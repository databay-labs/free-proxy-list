# Free proxy list API

`GET https://databay.com/api/v1/proxy-list` returns a current proxy snapshot for your signed-in Databay session. No purchase or API key is required. The website remains readable without signup; copying, selection, downloads and this API require an account. Previously published repository files are a separate distribution channel.

Browser requests use the active session cookie. For the cURL examples, `cookies.txt` must be a local cookie jar containing your own valid Databay session. Keep that file private. API responses and website exports are private/no-store and must not be shared through a cache.

```bash
curl --fail --show-error --silent --max-time 20 -b cookies.txt \
  "https://databay.com/api/v1/proxy-list?protocol=socks5&ssl=strict&limit=10"
```

## Filters and pagination

Omit a filter to include all matching records. Send each parameter at most once, use the spelling below, and omit empty values. Unknown parameters, repeated parameters, and invalid values return HTTP `400`.

| Parameter | Values | Default / meaning |
| --- | --- | --- |
| `protocol` | `http`, `https`, `socks4`, `socks5` | All. `https` selects HTTPS-capable proxies across protocols; it is not a separate connection scheme. |
| `country` | Two-letter ISO code, such as `US`, `DE`, `IN` | All countries; `XK` is also accepted. |
| `ssl` | `strict`, `loose` | All. `strict` requires destination HTTPS support with certificate validation; `loose` includes all HTTPS-capable proxies, including strict ones. Proxy-hop certificate validation is reported separately. |
| `anonymity` | `elite`, `anonymous`, `transparent` | All anonymity levels. |
| `google` | `true`, `false` | `true` requires a successful Google check. Omitted or `false` adds no filter. |
| `speed` | `fast`, `medium`, `slow` | `fast`: below 500 ms; `medium`: below 1,500 ms (includes fast); `slow`: at least 1,500 ms. |
| `format` | `json`, `csv`, `txt` | `json` |
| `limit` | Integer from `1` to `1000` | `500` records per page |
| `page` | Integer from `1` to `50000` | `1` |

Records are ordered by most recent successful check. Pagination applies to all formats. The snapshot can change between requests, so pagination is not a fixed export: deduplicate endpoints when combining pages. Cache your results and respect the response's `Cache-Control` and `Retry-After` headers.

## JSON response

Illustrative record; `192.0.2.1` is a documentation address, not a working proxy:

```json
{
  "data": [{
    "ip": "192.0.2.1",
    "port": 1080,
    "country": "Germany",
    "iso": "DE",
    "protocol": "Socks5",
    "proxyUrl": "socks5://192.0.2.1:1080",
    "ssl": true,
    "requiresLooseSsl": false,
    "requiresLooseProxyTls": false,
    "anonymity": "elite",
    "google": false,
    "latency": 420,
    "uptime": 95.2,
    "lastChecked": "2026-09-05T12:00:00Z"
  }],
  "page": 1,
  "limit": 10,
  "total": 1
}
```

`data` is the current page; `total` counts all records matching the filters before pagination. An empty `data` array is valid, including when there are no matches or the requested page is past the end.

| Field | Meaning |
| --- | --- |
| `ip`, `port` | Proxy address (string) and port (integer). |
| `country`, `iso` | Country name and two-letter country code. |
| `protocol` | Verified transport flags as a string, such as `Http`, `Https`, `Socks5`, or `Http, Socks5`. `Https` here means TLS to the proxy itself; the query filter `protocol=https` retains its broader destination-capability meaning. |
| `proxyUrl` | Proxy connection URI with its verified transport scheme. Use this instead of inferring the scheme from `ssl`. |
| `ssl` | Boolean HTTPS capability. It does not itself indicate strict certificate validation; request `ssl=strict` for that filter. |
| `requiresLooseSsl` | Whether destination TLS required relaxed certificate validation. |
| `requiresLooseProxyTls` | Whether the separate TLS connection to an HTTPS proxy required an unverified proxy certificate. This does not relax destination certificate validation. |
| `anonymity` | `elite`, `anonymous`, or `transparent`. |
| `google` | Whether the Google connectivity check succeeded. |
| `latency` | Latency at verification, in milliseconds (integer). |
| `uptime` | Percentage of successful checks over the endpoint's recorded checks (number). |
| `lastChecked` | Last successful verification in UTC, formatted as an ISO 8601 timestamp. |

These are observations at check time. They do not guarantee that a proxy still works for your network or destination. Keep TLS certificate verification enabled and use connection/read timeouts when trying an endpoint.

## TXT and CSV

```bash
curl --fail --show-error --silent --max-time 20 -b cookies.txt \
  "https://databay.com/api/v1/proxy-list?protocol=http&ssl=strict&format=txt&limit=100"

curl --fail --show-error --silent --max-time 20 -b cookies.txt \
  "https://databay.com/api/v1/proxy-list?country=DE&ssl=strict&format=csv&limit=100"
```

API TXT output includes comment lines beginning with `#`, followed by `IP:PORT` entries for existing transports. Rows that require TLS to the proxy have an `https://IP:PORT` prefix. Preserve that prefix; skip comments and blank lines. Repository `.txt` files remain bare endpoints, with the transport identified by each filename. Its `https.txt` is a TLS-to-proxy list, unlike the website's HTTPS-capability route. A country/protocol file in `by-country/` can be absent when no entries are available.

When `requiresLooseProxyTls` is true, curl can use `--proxy https://IP:PORT --proxy-insecure`. That option affects the proxy certificate only; keep destination certificate validation enabled and do not use `--insecure`.

CSV includes this header; use a CSV parser because the protocol field can contain commas:

```text
ip,port,country,iso,protocol,ssl,anonymity,google,latency_ms,uptime_pct,last_checked,proxy_url,requires_loose_proxy_tls,requires_loose_destination_tls
```

## Errors and runnable examples

- HTTP `401`: sign in again. An expired, missing or invalid session cannot retrieve the list.
- HTTP `400`: fix the request. The JSON body contains `error` and `retryable: false`.
- HTTP `429`: wait for `Retry-After` before retrying.
- HTTP `503`: the current inventory is unavailable. Wait according to `Retry-After`; do not treat an error response as an empty list.
- Other non-success responses and network timeouts: stop or use a bounded retry policy. Do not poll continuously.

Run these examples from a local clone with `DATABAY_SESSION_COOKIE` set locally to your own session cookie header. Do not commit or print it:

```bash
# Python 3.10+: download and print up to 10 strict SOCKS5 endpoints.
python examples/python_requests.py

# Optional: try at most 3 endpoints against https://example.com/.
python -m pip install "requests[socks]"
python examples/python_requests.py --try-proxy

# Node.js 22+: download and print the list using built-in fetch.
node examples/node_fetch.mjs
```

The [Python example](../examples/python_requests.py) downloads with the standard library. Its optional proxy request uses [Requests' SOCKS support](https://requests.readthedocs.io/en/latest/user/advanced/#socks) and `socks5h` for DNS resolution through the proxy. The [Node.js example](../examples/node_fetch.mjs) uses [built-in fetch](https://nodejs.org/api/globals.html#fetch) to retrieve the list; it does not route a destination request through a listed proxy.
