#!/usr/bin/env python3
"""Fetch strict SOCKS5 endpoints; optionally try a small sample with Requests.

Python 3.10+. Downloading the list needs no packages. For --try-proxy:
    python -m pip install "requests[socks]"
"""

import argparse
import ipaddress
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


API_URL = "https://databay.com/api/v1/proxy-list"
MAX_BODY_BYTES = 1_000_000
MAX_PROXY_ATTEMPTS = 3


def fetch_proxies():
    """Fetch one small page; raise on HTTP errors or an unexpected response."""
    query = urlencode({"protocol": "socks5", "ssl": "strict", "limit": 10})
    request = Request(f"{API_URL}?{query}", headers={
        "Accept": "application/json",
        "User-Agent": "databay-free-proxy-list-example/1.0 (+https://github.com/databay-labs/free-proxy-list)",
    })
    try:
        # urllib's timeout bounds socket operations, not the whole script.
        with urlopen(request, timeout=15) as response:
            body = response.read(MAX_BODY_BYTES + 1)
    except HTTPError as error:
        error.close()
        raise RuntimeError(f"List API returned HTTP {error.code}.") from error
    except (URLError, TimeoutError, OSError) as error:
        raise RuntimeError(f"List download failed: {error}") from error

    if len(body) > MAX_BODY_BYTES:
        raise ValueError("List response exceeded the 1 MB example limit.")
    payload = json.loads(body)
    if not isinstance(payload, dict) or not isinstance(payload.get("data"), list):
        raise ValueError("Expected a JSON object with a data array.")

    proxies = payload["data"]
    for proxy in proxies:
        if not isinstance(proxy, dict):
            raise ValueError("Expected a proxy object.")
        try:
            ipaddress.IPv4Address(proxy.get("ip"))
        except (ipaddress.AddressValueError, TypeError) as error:
            raise ValueError("Expected an IPv4 proxy address.") from error
        if type(proxy.get("port")) is not int or not 1 <= proxy["port"] <= 65535:
            raise ValueError("Expected a proxy port between 1 and 65535.")
        if "socks5" not in str(proxy.get("protocol", "")).lower().replace(" ", "").split(","):
            raise ValueError("Expected a SOCKS5 proxy in the filtered response.")
    return proxies


def try_sample(proxies):
    """Try up to three proxies once each, stopping after the first HTTP success."""
    try:
        import requests
        import socks  # noqa: F401 - verify that the optional SOCKS dependency exists
    except ImportError as error:
        raise RuntimeError('Install optional support: python -m pip install "requests[socks]"') from error

    with requests.Session() as session:
        # Keep ambient proxy settings and .netrc credentials out of this demo.
        session.trust_env = False
        for proxy in proxies[:MAX_PROXY_ATTEMPTS]:
            endpoint = f"{proxy['ip']}:{proxy['port']}"
            proxy_url = f"socks5h://{endpoint}"
            try:
                # No redirects, retries, credentials, or response body download.
                # TLS verification stays enabled. These are connect/read timeouts.
                with session.get(
                    "https://example.com/",
                    proxies={"http": proxy_url, "https": proxy_url},
                    timeout=(5, 10),
                    allow_redirects=False,
                    stream=True,
                ) as response:
                    response.raise_for_status()
                    if not 200 <= response.status_code < 300:
                        print(f"{endpoint}: HTTP {response.status_code}; trying the next candidate.", file=sys.stderr)
                        continue
                    print(f"{endpoint}: destination returned HTTP {response.status_code}.")
                    return True
            except requests.RequestException as error:
                print(f"{endpoint}: {type(error).__name__}; trying the next candidate.", file=sys.stderr)
    print("No sampled proxy succeeded. Fetch a fresh list later or change filters.", file=sys.stderr)
    return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--try-proxy", action="store_true", help="try at most three proxies against example.com")
    args = parser.parse_args()
    try:
        proxies = fetch_proxies()
        if not proxies:
            print("No matching proxies are available. Try again later or change filters.")
            return 0
        for proxy in proxies:
            print(f"{proxy['ip']}:{proxy['port']}")
        if args.try_proxy and not try_sample(proxies):
            return 1
        return 0
    except (RuntimeError, ValueError, UnicodeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
