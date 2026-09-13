# Free proxy list API

`GET https://databay.com/api/v1/proxy-list` returns a current proxy snapshot without an API key or signup. Use JSON for metadata and filtering, or the [repository's raw files](https://github.com/databay-labs/free-proxy-list#readme) for a plain `IP:PORT` list.

```bash
curl --fail --show-error --silent --max-time 20 \
  "https://databay.com/api/v1/proxy-list?protocol=socks5&ssl=strict&limit=10"
```

## Filters and pagination

Omit a filter to include all matching records. Send each parameter at most once, use the spelling below, and omit empty values. Unknown parameters, repeated parameters, and invalid values return HTTP `400`.

| Parameter | Values | Default / meaning |
| --- | --- | --- |
| `protocol` | `http`, `https`, `socks4`, `socks5` | All. `https` selects HTTPS-capable proxies across protocols; it is not a separate connection scheme. |
| `country` | Two-letter ISO code, such as `US`, `DE`, `IN` | All countries; `XK` is also accepted. |
| `ssl` | `strict`, `loose` | All. `strict` requires HTTPS support with certificate validation; `loose` includes all HTTPS-capable proxies, including strict ones. |
| `anonymity` | `elite`, `anonymous`, `transparent` | All anonymity levels. |
| `google` | `true`, `false` | `true` requires a successful Google check. Omitted or `false` adds no filter. |
| `speed` | `fast`, `medium`, `slow` | `fast`: below 500 ms; `medium`: below 1,500 ms (includes fast); `slow`: at least 1,500 ms. |
| `format` | `json`, `csv`, `txt` | `json` |
| `limit` | Integer from `1` to `1000` | `500` records per page |
| `page` | Integer from `1` to `1000` | `1` |

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
    "ssl": true,
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
| `protocol` | Supported protocol flags as a string, such as `Http`, `Socks5`, or `Http, Socks5`. Split on commas and trim when checking individual flags. |
| `ssl` | Boolean HTTPS capability. It does not itself indicate strict certificate validation; request `ssl=strict` for that filter. |
| `anonymity` | `elite`, `anonymous`, or `transparent`. |
| `google` | Whether the Google connectivity check succeeded. |
| `latency` | Latency at verification, in milliseconds (integer). |
| `uptime` | Percentage of successful checks over the endpoint's recorded checks (number). |
| `lastChecked` | Last successful verification in UTC, formatted as an ISO 8601 timestamp. |

These are observations at check time. They do not guarantee that a proxy still works for your network or destination. Keep TLS certificate verification enabled and use connection/read timeouts when trying an endpoint.

## TXT and CSV

```bash
curl --fail --show-error --silent --max-time 20 \
  "https://databay.com/api/v1/proxy-list?protocol=http&ssl=strict&format=txt&limit=100"

curl --fail --show-error --silent --max-time 20 \
  "https://databay.com/api/v1/proxy-list?country=DE&ssl=strict&format=csv&limit=100"
```

API TXT output includes comment lines beginning with `#`, followed by `IP:PORT` entries. Skip comments and blank lines when parsing it. Repository `.txt` files contain endpoint lines without those comments. A country/protocol file in `by-country/` can be absent when no entries are available.

CSV includes this header; use a CSV parser because the protocol field can contain commas:

```text
ip,port,country,iso,protocol,ssl,anonymity,google,latency_ms,uptime_pct,last_checked
```

## Errors and runnable examples

- HTTP `400`: fix the request. The JSON body contains `error` and `retryable: false`.
- HTTP `503`: the current inventory is unavailable. Wait according to `Retry-After`; do not treat an error response as an empty list.
- Other non-success responses and network timeouts: stop or use a bounded retry policy. Do not poll continuously.

Run these examples from a local clone:

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
