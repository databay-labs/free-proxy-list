# Free Proxy List — HTTP/HTTPS, SOCKS4 & SOCKS5

Download public proxies as plain `IP:PORT` files, filter by country, or use the free JSON, CSV and TXT API. No account or API key is required. Maintained by [Databay](https://databay.com/free-proxy-list?utm_source=github&utm_medium=repository&utm_campaign=free_proxy_list&utm_content=intro).

[Download lists](#download-proxy-lists) · [Quick start](#quick-start) · [API reference](docs/api.md) · [Examples](examples/) · [Contribute](CONTRIBUTING.md)

**If this list helps your project, [star the repository](https://github.com/databay-labs/free-proxy-list) to find it again and support its maintenance.**

## Download proxy lists

Each GitHub file contains one `IP:PORT` per line, without headers. Entries passed an HTTPS request with destination certificate validation at their last successful check.

| Protocol | Published entries | Direct download |
| --- | ---: | --- |
| HTTP (CONNECT for HTTPS destinations) | 3447 | [http.txt](https://raw.githubusercontent.com/databay-labs/free-proxy-list/master/http.txt) |
| SOCKS4 | 768 | [socks4.txt](https://raw.githubusercontent.com/databay-labs/free-proxy-list/master/socks4.txt) |
| SOCKS5 | 343 | [socks5.txt](https://raw.githubusercontent.com/databay-labs/free-proxy-list/master/socks5.txt) |

The publisher runs on a five-minute schedule. Lists can remain unchanged between publications, and raw/CDN caches can lag. A listed endpoint can stop working between checks; see [verification and freshness](#verification-and-freshness).

## Quick start

Download the HTTP list with curl:

```bash
curl --fail --show-error --location --max-time 30 \
  https://raw.githubusercontent.com/databay-labs/free-proxy-list/master/http.txt \
  --output http.txt
```

Try an HTTPS request through one entry, replacing `IP:PORT` with a downloaded endpoint:

```bash
curl --fail --show-error --connect-timeout 5 --max-time 15 \
  --proxy http://IP:PORT https://example.com
```

For SOCKS5, use `--proxy socks5h://IP:PORT` so the proxy resolves the destination hostname. Keep TLS certificate verification enabled. On Windows PowerShell, call `curl.exe` to avoid the legacy `curl` alias.

**Want to filter visually?** [Browse the free proxy list](https://databay.com/free-proxy-list?utm_source=github&utm_medium=repository&utm_campaign=free_proxy_list&utm_content=browse) by country, protocol, latency and anonymity, then export the result.

### Alternative download endpoints

The same GitHub files are also available through [jsDelivr](https://cdn.jsdelivr.net/gh/databay-labs/free-proxy-list@master/http.txt); replace `http.txt` with `socks4.txt` or `socks5.txt`. CDN caching can delay updates.

Databay also serves [all protocols](https://databay.com/free-proxy-list.txt), [HTTP](https://databay.com/free-proxy-list/http.txt), [HTTPS-capable](https://databay.com/free-proxy-list/https.txt), [SOCKS4](https://databay.com/free-proxy-list/socks4.txt) and [SOCKS5](https://databay.com/free-proxy-list/socks5.txt) TXT exports. These can include a broader pool than the GitHub files and contain `#` comment headers; skip those lines when parsing. Use the API with `ssl=strict` when you need the GitHub TLS eligibility policy.

## Filter by country

Browse [`by-country/`](by-country/) for lowercase ISO country-code directories. Each country includes only the protocol files with available entries; an absent combination returns 404.

```bash
# US HTTP proxies, if currently available
curl --fail --show-error --location --max-time 30 \
  https://raw.githubusercontent.com/databay-labs/free-proxy-list/master/by-country/us/http.txt \
  --output us-http.txt
```

For a filter that returns an empty result instead of a missing file, use the API:

```bash
curl --fail --show-error --max-time 30 \
  'https://databay.com/api/v1/proxy-list?country=US&protocol=http&ssl=strict&limit=20'
```

You can also browse the [country directory](https://databay.com/free-proxy-list/directory?utm_source=github&utm_medium=repository&utm_campaign=free_proxy_list&utm_content=countries) to choose a country visually.

## Free proxy API

`GET https://databay.com/api/v1/proxy-list`

Choose `protocol`, `country`, `anonymity`, `ssl`, `google` and `speed`; export with `format=json`, `format=csv` or `format=txt`. JSON responses contain `data`, `page`, `limit` and `total`. The default limit is 500; each page can contain up to 1,000 records.

```bash
# SOCKS5 proxies that passed destination certificate validation
curl --fail --show-error --max-time 30 \
  'https://databay.com/api/v1/proxy-list?protocol=socks5&ssl=strict&limit=20'

# HTTP proxies from Germany as CSV
curl --fail --show-error --max-time 30 \
  'https://databay.com/api/v1/proxy-list?protocol=http&country=DE&ssl=strict&format=csv' \
  --output de-http.csv
```

Use `ssl=strict` to select the same TLS eligibility policy as the GitHub lists. The website/API can expose a broader pool, so its totals may differ. `protocol=https` selects HTTPS-capable endpoints across transports; use `protocol=http&ssl=strict` when you need an HTTP CONNECT proxy.

See the [full API reference](docs/api.md) for fields, filter behavior, pagination and errors. Cache downloads locally for repeated jobs. Databay's TXT exports include comment headers; GitHub TXT files contain only endpoints.

## Python and Node.js examples

The [Python example](examples/python_requests.py) fetches a SOCKS5 list and can make a bounded trial request. The [Node.js example](examples/node_fetch.mjs) fetches and prints proxy records using built-in `fetch`. Both handle HTTP errors and empty results.

Run from a local clone with Python 3.10+ or Node.js 22+:

```bash
python examples/python_requests.py
node examples/node_fetch.mjs
```

Fetching the list does not configure a proxy for subsequent requests. The examples explain the separate client configuration step.

## Verification and freshness

- Candidates come from public feeds and are checked by Databay before publication.
- GitHub exports require a successful HTTPS request with destination certificate validation. Endpoints requiring relaxed certificate validation are excluded.
- A recent successful check qualifies an entry for publication for up to six hours. Publication time does not mean every endpoint was retested at that instant. The API's `lastChecked` field gives each record's last successful check.
- Within each protocol file, the publisher keeps one endpoint per IP, preferring higher observed uptime and then lower measured latency. The same IP can appear in more than one protocol or country view, so adding file counts does not give a distinct global IP count.
- Measurements describe the checker's connection to its test destination. They do not establish future availability, speed from your location, operator trust, or access to other sites.

An HTTP proxy in `http.txt` uses CONNECT to reach HTTPS destinations; this does not mean the connection to the proxy itself accepts `https://`. There is no separate `https.txt` in this repository.

Public proxies can observe connection metadata and unencrypted traffic. Keep certificate verification enabled, avoid sending credentials or sensitive data, and use only destinations and request rates you are authorized to access.

## Troubleshooting

| Symptom | Next step |
| --- | --- |
| Connection timeout or refused connection | Download a fresh list and try another entry with a bounded timeout. Availability varies by location and destination. |
| SOCKS support missing in Python | Install `requests[socks]` for the optional proxy request in the Python example. |
| Country file returns 404 | Check [`by-country/`](by-country/) or use a country filter in the API; available combinations change. |
| API returns an empty `data` array | Reduce the filters or retry later; zero matching proxies is a valid response. |
| API and GitHub counts differ | Request `ssl=strict`, account for pagination, and compare collection times. |
| Clone or pull conflicts after an update | Download raw files for routine use. The publisher currently rewrites the snapshot commit; this is a dataset feed, not a stable commit history. |

## Help improve the list

Contributions to examples, documentation and candidate-source coverage are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before editing generated files. If you use the list in a tutorial or tool, linking back helps other developers find the data and its limitations.

For a broken download or API regression, include the URL, UTC time, response status and a small reproducible example in your report. One dead endpoint does not establish a feed outage: individual public proxies frequently disappear. See the contribution guide for the available contact route.

## Maintainer and license

Maintained by [Databay](https://databay.com/?utm_source=github&utm_medium=repository&utm_campaign=free_proxy_list&utm_content=maintainer), which also offers commercial proxy services. This public dataset, its documentation and the examples require no purchase. The scraper service's implementation is not included in this repository.

Databay's original material is released under the [MIT License](LICENSE). Third-party source compilations retain their respective licenses and attribution requirements.

This dataset is provided as-is. Review the verification limits above and respect the [GitHub Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies).
