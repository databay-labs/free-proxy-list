<div align="center">

<a href="https://databay.com/proxies/residential" target="_blank" title="Get Databay Premium Residential Proxies"><img width="100%" alt="Databay logo" src="https://raw.githubusercontent.com/databay-labs/free-proxy-list/master/databay-banner.png"></a>

# 🔄 Free Proxy List by Databay.com | Constantly Updated

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Updated every 5 minutes](https://img.shields.io/badge/Updated-Every%205%20mins-brightgreen)
![Strict SSL Validated](https://img.shields.io/badge/SSL-Strict%20%E2%9C%93%20No%20MITM-success)
<img src="https://img.shields.io/badge/Last%20Update-0.26%20second(s)%20ago-blueviolet">
<img src="https://img.shields.io/badge/Countries-110%2B-orange">

</br>

<a href="https://github.com/databay-labs/free-proxy-list/raw/refs/heads/master/http.txt">
  <img src="https://img.shields.io/badge/HTTP-1384%20PROXIES-brightgreen">
</a>
<a href="https://github.com/databay-labs/free-proxy-list/raw/refs/heads/master/socks4.txt">
  <img src="https://img.shields.io/badge/SOCKS4-571%20PROXIES-orange">
</a>
<a href="https://github.com/databay-labs/free-proxy-list/raw/refs/heads/master/socks5.txt">
  <img src="https://img.shields.io/badge/SOCKS5-258%20PROXIES-blue">
</a>

</br>

![Latency](https://img.shields.io/badge/Avg%20Latency-2650ms-yellow)
![Lowest](https://img.shields.io/badge/Lowest%20Latency-55ms-brightgreen)

**&searr;&nbsp;&nbsp;Browse, filter & download the full list with API access&nbsp;&nbsp;&swarr;**

[**Browse the live Free Proxy List (filter, country pages, API) →**](https://databay.com/free-proxy-list)

</div>

> [!IMPORTANT]\
> ⚠️ Free proxies carry risks! Many perform MITM attacks to modify your data. **All proxies in this list have valid SSL certificates** (strict HTTPS — no MITM certificate trust needed). For secure browsing at scale, consider **[Databay's Premium Rotating Proxies](https://databay.com/)**.

---

## 📑 Table of Contents

- [🚀 Features](#-features)
- [📥 Quick Start — Direct Downloads](#-quick-start--direct-downloads)
- [🌍 Country-Specific Lists](#-country-specific-lists)
- [🌐 Free Public API](#-free-public-api)
  - [Query Parameters](#query-parameters)
  - [Example Requests](#example-requests)
  - [Response Schema](#response-schema)
- [💻 Code Examples](#-code-examples)
  - [Python](#-python)
  - [Node.js](#-nodejs)
  - [Go](#-go)
  - [PHP](#-php)
  - [Java](#-java)
  - [C# / .NET](#-c--net)
- [🛡️ Why Strict SSL Matters](#%EF%B8%8F-why-strict-ssl-matters)
- [🚀 Need Premium?](#-need-premium)
- [📜 License](#-license)
- [⚠️ Disclaimer](#%EF%B8%8F-disclaimer)

---

## 🚀 Features

- **🔒 Strict SSL Validated**: Every proxy correctly tunnels HTTPS traffic and preserves the target site's SSL certificate (no MITM)
- **🕒 Refreshed Every 5 Minutes**: Always-fresh, never-stale list
- **✨ Zero Duplicates**: Each commit is deduplicated and sorted by recency
- **🌍 Multi-Country**: Proxies from **110+ countries** with per-country breakdowns
- **🚦 Multi-Protocol**:
  - **HTTP**: 1384 proxies (CONNECT method for HTTPS sites — strict SSL)
  - **SOCKS4**: 571 proxies
  - **SOCKS5**: 258 proxies
- **⚡ Low Latency**: avg 2650ms, best 55ms
- **🔓 No Auth Required**: All resources are public — no API key needed for the free tier

> **Note on `https.txt`:** there is no separate HTTPS file in this repository. Modern HTTP proxies tunnel HTTPS via the `CONNECT` method, and **every proxy in `http.txt` has been verified to do this without breaking SSL certificate trust**. This is the unique guarantee of this list. (The databay.com origin additionally serves an [https.txt hotlink](https://databay.com/free-proxy-list/https.txt) filtered to verified-HTTPS proxies.)

---

## 📥 Quick Start — Direct Downloads

Each file is plain text, one `IP:PORT` per line.

### Hotlink from databay.com (always-on origin, 5-min refresh, CORS-open)

Permanent, unauthenticated URLs served straight from the origin — no API key, no signup, stable enough to hardcode in scripts, CI and tutorials:

```bash
# Full list (all protocols)
curl -s https://databay.com/free-proxy-list.txt

# Per protocol
curl -s https://databay.com/free-proxy-list/http.txt
curl -s https://databay.com/free-proxy-list/socks5.txt

# Per country (canonical country slug)
curl -s https://databay.com/free-proxy-list/united-states-of-america.txt
```

### jsDelivr CDN mirrors (bandwidth-friendly alternative)

#### HTTP Proxies (Strict SSL)
```bash
curl -O https://cdn.jsdelivr.net/gh/databay-labs/free-proxy-list/http.txt
```

#### SOCKS4 Proxies (Strict SSL)
```bash
curl -O https://cdn.jsdelivr.net/gh/databay-labs/free-proxy-list/socks4.txt
```

#### SOCKS5 Proxies (Strict SSL)
```bash
curl -O https://cdn.jsdelivr.net/gh/databay-labs/free-proxy-list/socks5.txt
```

You can also use the raw GitHub URL if you prefer:
```bash
curl -O https://raw.githubusercontent.com/databay-labs/free-proxy-list/master/http.txt
```

---

## 🌍 Country-Specific Lists

Need proxies from a specific country? Browse the [`by-country/`](./by-country/) directory — each country has its own folder with `http.txt`, `socks4.txt`, and `socks5.txt` (only the protocol files that actually have proxies for that country are shipped).

```bash
# US SOCKS5 proxies
curl -O https://cdn.jsdelivr.net/gh/databay-labs/free-proxy-list/by-country/us/socks5.txt

# Germany HTTP proxies
curl -O https://cdn.jsdelivr.net/gh/databay-labs/free-proxy-list/by-country/de/http.txt

# United Kingdom SOCKS4 proxies
curl -O https://cdn.jsdelivr.net/gh/databay-labs/free-proxy-list/by-country/gb/socks4.txt
```

Country codes follow the [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) standard, lowercased.

**Browse by country** — every country also has a live, filterable page on databay.com with uptime, latency, SSL and anonymity columns:
[United States free proxy list](https://databay.com/free-proxy-list/united-states-of-america) ·
[Germany free proxy list](https://databay.com/free-proxy-list/germany) ·
[United Kingdom free proxy list](https://databay.com/free-proxy-list/united-kingdom) ·
[France free proxy list](https://databay.com/free-proxy-list/france) ·
[Brazil free proxy list](https://databay.com/free-proxy-list/brazil) ·
[India free proxy list](https://databay.com/free-proxy-list/india) ·
[Indonesia free proxy list](https://databay.com/free-proxy-list/indonesia) ·
[Singapore free proxy list](https://databay.com/free-proxy-list/singapore) ·
[Canada free proxy list](https://databay.com/free-proxy-list/canada) ·
[Netherlands free proxy list](https://databay.com/free-proxy-list/netherlands) ·
[full country directory](https://databay.com/free-proxy-list/directory)

---

## 🌐 Free Public API

For richer filtering (anonymity level, Google compatibility, speed, country) and more export formats, hit the **public, unauthenticated** Databay API:

```
GET https://databay.com/api/v1/proxy-list
```

No API key. No signup. Just `curl` and go.

### Query Parameters

| Parameter | Accepted Values | Default | Description |
|-----------|-----------------|---------|-------------|
| `protocol` | `http`, `https`, `socks4`, `socks5` | all | Filter by protocol |
| `country` | ISO 2-letter code (`US`, `DE`, `CN`, …) | all | Filter by country |
| `anonymity` | `elite`, `anonymous`, `transparent` | all | Filter by anonymity level |
| `ssl` | `strict`, `loose` | all | `strict` = no MITM, valid certificate; `loose` includes invalid-cert proxies |
| `google` | `true` | all | Only proxies that work for Google services |
| `speed` | `fast`, `medium`, `slow` | all | Latency tier |
| `format` | `json`, `csv`, `txt` | `json` | Output format |
| `limit` | `1`–`1000` | `500` | Proxies per page |
| `page` | `1+` | `1` | Page number for pagination |

**Access:** No API key and no application-level request limit. Responses are cached for 15 seconds.

### Example Requests

```bash
# All strict-SSL proxies as JSON
curl "https://databay.com/api/v1/proxy-list?ssl=strict"

# Elite SOCKS5 proxies, US only
curl "https://databay.com/api/v1/proxy-list?protocol=socks5&anonymity=elite&country=US&ssl=strict"

# Google-compatible proxies as plain text
curl "https://databay.com/api/v1/proxy-list?google=true&ssl=strict&format=txt"

# Fast proxies as CSV (paginated)
curl "https://databay.com/api/v1/proxy-list?speed=fast&format=csv&limit=100&page=2"
```

### Response Schema

JSON responses are wrapped in an envelope:

```json
{
  "data": [ { "...proxy record..." } ],
  "page": 1,
  "limit": 500,
  "total": 1234
}
```

Each proxy record in `data` contains:

| Field | Type | Description |
|-------|------|-------------|
| `ip` | string | Proxy IPv4 address |
| `port` | integer | Proxy port |
| `country` | string | Country name (e.g. `United States`) |
| `iso` | string | ISO 2-letter country code (e.g. `US`) |
| `protocol` | string | Protocol flags, e.g. `Http`, `Socks5`, `Http, Socks5` |
| `ssl` | boolean | `true` when the proxy tunnels HTTPS |
| `anonymity` | string | `elite` / `anonymous` |
| `google` | boolean | Reachable for Google services |
| `latency` | integer | Last verified latency in ms |
| `uptime` | float | Lifetime uptime % |
| `lastChecked` | ISO 8601 | Timestamp of last verification (UTC) |

---

## 💻 Code Examples

All examples below pull the JSON-formatted strict-SSL list from the API and read the `data` envelope property. Drop the API call and use the `.txt` direct downloads if you don't need filtering.

### 🐍 Python

```python
import requests

resp = requests.get(
    "https://databay.com/api/v1/proxy-list",
    params={"ssl": "strict", "protocol": "socks5", "format": "json"},
    timeout=10,
)
proxies = resp.json()["data"]

for p in proxies:
    print(f"{p['ip']}:{p['port']}  ({p['iso']}, {p['latency']}ms, {p['anonymity']})")
```

Use one with the `requests` library:
```python
proxy = proxies[0]
url_proxy = f"socks5://{proxy['ip']}:{proxy['port']}"
r = requests.get("https://example.com", proxies={"http": url_proxy, "https": url_proxy})
```

### 🟢 Node.js

```javascript
const res = await fetch(
  "https://databay.com/api/v1/proxy-list?ssl=strict&protocol=socks5"
);
const { data } = await res.json();

for (const p of data) {
  console.log(`${p.ip}:${p.port}  (${p.iso}, ${p.latency}ms, ${p.anonymity})`);
}
```

### 🐹 Go

```go
package main

import (
    "encoding/json"
    "fmt"
    "net/http"
)

type Proxy struct {
    IP        string `json:"ip"`
    Port      int    `json:"port"`
    Iso       string `json:"iso"`
    Protocol  string `json:"protocol"`
    Latency   int    `json:"latency"`
}

type Envelope struct {
    Data  []Proxy `json:"data"`
    Total int     `json:"total"`
}

func main() {
    resp, _ := http.Get("https://databay.com/api/v1/proxy-list?ssl=strict")
    defer resp.Body.Close()

    var envelope Envelope
    json.NewDecoder(resp.Body).Decode(&envelope)

    for _, p := range envelope.Data {
        fmt.Printf("%s:%d (%s, %dms)\n", p.IP, p.Port, p.Iso, p.Latency)
    }
}
```

### 🐘 PHP

```php
<?php
$json = file_get_contents("https://databay.com/api/v1/proxy-list?ssl=strict");
$response = json_decode($json, true);

foreach ($response['data'] as $p) {
    echo "{$p['ip']}:{$p['port']} ({$p['iso']}, {$p['latency']}ms)\n";
}
```

### ☕ Java

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

HttpClient client = HttpClient.newHttpClient();
HttpRequest req = HttpRequest.newBuilder()
    .uri(URI.create("https://databay.com/api/v1/proxy-list?ssl=strict&protocol=socks5"))
    .build();

HttpResponse<String> resp = client.send(req, HttpResponse.BodyHandlers.ofString());
System.out.println(resp.body());
// Parse with Jackson/Gson - records are under the top-level "data" array
```

### 🟣 C# / .NET

```csharp
using System.Net.Http.Json;

var http = new HttpClient();
var envelope = await http.GetFromJsonAsync<Envelope>(
    "https://databay.com/api/v1/proxy-list?ssl=strict&protocol=socks5"
);

foreach (var p in envelope!.Data!)
    Console.WriteLine($"{p.Ip}:{p.Port} ({p.Iso}, {p.Latency}ms)");

record Proxy(string Ip, int Port, string Iso, string Protocol, int Latency);
record Envelope(List<Proxy> Data, int Page, int Limit, int Total);
```

---

## 🛡️ Why Strict SSL Matters

Most "free proxy lists" don't validate that the proxies they ship preserve target SSL certificates. A large fraction of free proxies actively **MITM your HTTPS traffic** — they decrypt it, optionally inject content, and re-encrypt with their own certificate. Apps that disable certificate validation (depressingly common in scrapers) leak credentials and private data straight to the proxy operator.

This list ships **only proxies that passed HTTPS verification against our test target with a valid target certificate**. Proxies requiring relaxed certificate validation are filtered out of the published protocol files. This is evidence from the recorded check, not a guarantee about other destinations or future connections.

For production-grade scraping, browsing, or automation, even strict-SSL free proxies are unreliable (low uptime, shared IPs flagged everywhere). Consider Databay's premium rotating proxies for that workload.

---

## 🚀 Need Premium?

Free proxies are great for testing and one-off jobs, but they share IPs with thousands of other users — meaning they're rate-limited, banned, or blacklisted on most major sites.

[**Databay's premium proxies**](https://databay.com/) give you:

- ✅ **Cumulative historical catalogue totals:** 34M+ Residential IPs, 800K+ Mobile IPs, and 80K+ Datacenter IPs; not current live availability
- ✅ **Residential Flex access** over residential-origin capacity
- ✅ **195 published paid-location route pages** in the location catalogue
- ✅ **Connection-aware rotation** — a new proxy connection may select a new IP; reuse may retain one, so a fresh IP is not guaranteed
- ✅ **Zero MITM** — fully encrypted HTTPS traffic
- ✅ **Expert support** — direct access to engineers

🔗 [**Get Databay Premium Proxies →**](https://databay.com/)

---

## 📜 License

Databay's original material is released under the [MIT License](LICENSE). Third-party source compilations retain their respective licenses and attribution requirements.

Candidate sources include [Proxmint's Free Proxy List](https://proxmint.com/free-proxies) ([source compilation](https://github.com/proxmint/free-proxy-list)) and [Proxio's Proxy List](https://proxio.io) ([source compilation](https://github.com/proxio-io/proxy-list)), both published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Databay combines, deduplicates, independently checks and filters these candidates; the results here differ from those source compilations. Please preserve these credits when redistributing derived lists.

Additional candidate feeds include [HProxy](https://github.com/hproxy-com/free-proxy-list) and [Relayglass](https://github.com/relayglass/free-proxy-list). Source labels are independently checked by Databay before publication. The expanded feed inventory is listed in [candidate source credits](SOURCE_CREDITS.md).

---

## ⚠️ Disclaimer

**This proxy list is provided "as-is".** We are not responsible for any misuse or damages. Use at your own risk. Always prioritize security and respect the [GitHub Acceptable Use Policy](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies) and the laws of your jurisdiction.
