# Free Proxy List — HTTP/HTTPS, SOCKS4 & SOCKS5

Download public proxies as plain `IP:PORT` GitHub files without an account or API key. Databay's website exports and JSON, CSV and TXT API require Databay sign-in. Maintained by [Databay](https://databay.com/free-proxy-list?utm_source=github&utm_medium=repository&utm_campaign=free_proxy_list&utm_content=intro).

[Download lists](#download-proxy-lists) · [Quick start](#quick-start) · [API reference](docs/api.md) · [Examples](examples/) · [Contribute](CONTRIBUTING.md)

**If this list helps your project, [star the repository](https://github.com/databay-labs/free-proxy-list) to find it again and support its maintenance.**

## Download proxy lists

Each GitHub file contains one `IP:PORT` per line, without headers. Entries passed an HTTPS request with destination certificate validation at their last successful check.

**9921 distinct proxy endpoints across 9813 IP addresses.** An endpoint is an IP address and port; one IP can host several working endpoints. The protocol files overlap, so adding their row counts does not give the total endpoint count.

| Protocol | Published entries | Direct download |
| --- | ---: | --- |
| HTTP (CONNECT for HTTPS destinations) | 6387 | [http.txt](https://raw.githubusercontent.com/databay-labs/free-proxy-list/master/http.txt) |
| HTTPS proxy (TLS to the proxy) | 1820 | [https.txt](https://raw.githubusercontent.com/databay-labs/free-proxy-list/master/https.txt) |
| SOCKS4 | 1111 | [socks4.txt](https://raw.githubusercontent.com/databay-labs/free-proxy-list/master/socks4.txt) |
| SOCKS5 | 603 | [socks5.txt](https://raw.githubusercontent.com/databay-labs/free-proxy-list/master/socks5.txt) |

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

Entries from `https.txt` require an encrypted connection to the proxy itself:

```bash
curl --fail --show-error --connect-timeout 5 --max-time 15 \
  --proxy https://IP:PORT --proxy-insecure https://example.com
```

`--proxy-insecure` permits an unverified certificate on the proxy hop only. The destination certificate remains verified; do not replace it with `--insecure`. The HTTPS proxy file can include self-signed proxy certificates. The website/API's `requiresLooseProxyTls` field distinguishes that condition from destination TLS validation.

**Want to filter visually?** [Browse the free proxy list](https://databay.com/free-proxy-list?utm_source=github&utm_medium=repository&utm_campaign=free_proxy_list&utm_content=browse) by country, protocol, latency and anonymity, then export the result.

### Alternative download endpoints

The same GitHub files are also available through [jsDelivr](https://cdn.jsdelivr.net/gh/databay-labs/free-proxy-list@master/http.txt); replace `http.txt` with `https.txt`, `socks4.txt` or `socks5.txt`. CDN caching can delay updates.

After sign-in, Databay also serves [all protocols](https://databay.com/free-proxy-list.txt), [HTTP](https://databay.com/free-proxy-list/http.txt), [HTTPS-capable](https://databay.com/free-proxy-list/https.txt), [SOCKS4](https://databay.com/free-proxy-list/socks4.txt) and [SOCKS5](https://databay.com/free-proxy-list/socks5.txt) TXT exports. These can include a broader pool than the GitHub files and contain `#` comment headers; skip those lines when parsing. Website TXT rows that require TLS to the proxy retain an `https://` prefix. Use the API with `ssl=strict` when you need the GitHub destination TLS eligibility policy.

## Filter by country

Browse [`by-country/`](by-country/) for lowercase ISO country-code directories. Each country includes only the protocol files with available entries; an absent combination returns 404.

```bash
# US HTTP proxies, if currently available
curl --fail --show-error --location --max-time 30 \
  https://raw.githubusercontent.com/databay-labs/free-proxy-list/master/by-country/us/http.txt \
  --output us-http.txt
```

For a filter that returns an empty result instead of a missing file, use the API with a valid Databay session cookie stored locally in `cookies.txt`:

```bash
curl --fail --show-error --max-time 30 --cookie cookies.txt \
  'https://databay.com/api/v1/proxy-list?country=US&protocol=http&ssl=strict&limit=20'
```

You can also browse the [country directory](https://databay.com/free-proxy-list/directory?utm_source=github&utm_medium=repository&utm_campaign=free_proxy_list&utm_content=countries) to choose a country visually.

## Free proxy API

`GET https://databay.com/api/v1/proxy-list`

Website API requests require a valid Databay sign-in session. The examples below assume its cookie is stored locally in `cookies.txt`; anonymous requests are refused. Keep session cookies private.

Choose `protocol`, `country`, `anonymity`, `ssl`, `google` and `speed`; export with `format=json`, `format=csv` or `format=txt`. JSON responses contain `data`, `page`, `limit` and `total`. The default limit is 500; each page can contain up to 1,000 records.

```bash
# SOCKS5 proxies that passed destination certificate validation
curl --fail --show-error --max-time 30 --cookie cookies.txt \
  'https://databay.com/api/v1/proxy-list?protocol=socks5&ssl=strict&limit=20'

# HTTP proxies from Germany as CSV
curl --fail --show-error --max-time 30 --cookie cookies.txt \
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
- GitHub exports require a successful HTTPS request with destination certificate validation. Endpoints requiring relaxed destination certificate validation are excluded. The separate `https.txt` file may include unverified proxy-hop certificates, as described in the quick start.
- A recent successful check qualifies an entry for publication for up to six hours. Publication time does not mean every endpoint was retested at that instant. The API's `lastChecked` field gives each record's last successful check.
- Within each protocol file, the publisher keeps one endpoint per IP, preferring no consecutive failures, then the latest successful check, higher observed uptime, and lower measured latency. The same endpoint can appear in more than one protocol or country view. The endpoint and IP totals above deduplicate the root protocol files separately.
- Measurements describe the checker's connection to its test destination. They do not establish future availability, speed from your location, operator trust, or access to other sites.

An HTTP proxy in `http.txt` uses CONNECT to reach HTTPS destinations over a plain HTTP proxy connection. The separate `https.txt` contains verified TLS-to-proxy transports. The website's `/free-proxy-list/https.txt` route and API `protocol=https` filter instead mean destination HTTPS capability across transports; check each record's `proxyUrl` to select its connection scheme.

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
