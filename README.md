<div align="center">

<a href="https://databay.com/proxies/residential" target="_blank" title="Get Databay Premium Residential Proxies"><img width="100%" alt="Databay logo" src="https://raw.githubusercontent.com/databay-labs/free-proxy-list/master/databay-banner.png"></a>

# 🔄 Free Proxy List by Databay.com | Constantly Updated

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Updated every 5 minutes](https://img.shields.io/badge/Updated-Every%205%20mins-brightgreen)
![Strict SSL Validated](https://img.shields.io/badge/SSL-Strict%20%E2%9C%93%20No%20MITM-success)
<img src="https://img.shields.io/badge/Last%20Update-4%20second(s)%20ago-blueviolet">
<img src="https://img.shields.io/badge/Countries-102%2B-orange">

</br>

<a href="https://github.com/databay-labs/free-proxy-list/raw/refs/heads/master/http.txt">
  <img src="https://img.shields.io/badge/HTTP-2093%20PROXIES-brightgreen">
</a>
<a href="https://github.com/databay-labs/free-proxy-list/raw/refs/heads/master/socks4.txt">
  <img src="https://img.shields.io/badge/SOCKS4-683%20PROXIES-orange">
</a>
<a href="https://github.com/databay-labs/free-proxy-list/raw/refs/heads/master/socks5.txt">
  <img src="https://img.shields.io/badge/SOCKS5-3806%20PROXIES-blue">
</a>

</br>

![Latency](https://img.shields.io/badge/Avg%20Latency-1658ms-yellow)
![Lowest](https://img.shields.io/badge/Lowest%20Latency-55ms-brightgreen)

**&searr;&nbsp;&nbsp;Browse, filter & download the full list with API access&nbsp;&nbsp;&swarr;**

[**databay.com/free-proxy-list**](https://databay.com/free-proxy-list)

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
- **🌍 Multi-Country**: Proxies from **102+ countries** with per-country breakdowns
- **🚦 Multi-Protocol**:
  - **HTTP**: 2093 proxies (CONNECT method for HTTPS sites — strict SSL)
  - **SOCKS4**: 683 proxies
  - **SOCKS5**: 3806 proxies
- **⚡ Low Latency**: avg 1658ms, best 55ms
- **🔓 No Auth Required**: All resources are public — no API key needed for the free tier

> **Note on `https.txt`:** there is no separate HTTPS file. Modern HTTP proxies tunnel HTTPS via the `CONNECT` method, and **every proxy in `http.txt` has been verified to do this without breaking SSL certificate trust**. This is the unique guarantee of this list.

---

## 📥 Quick Start — Direct Downloads

Each file is plain text, one `IP:PORT` per line.

### HTTP Proxies (Strict SSL)
```bash
curl -O https://cdn.jsdelivr.net/gh/databay-labs/free-proxy-list/http.txt
```

### SOCKS4 Proxies (Strict SSL)
```bash
curl -O https://cdn.jsdelivr.net/gh/databay-labs/free-proxy-list/socks4.txt
```

### SOCKS5 Proxies (Strict SSL)
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
| `protocol` | `http`, `https`, `socks5` | all | Filter by protocol |
| `country` | ISO 2-letter code (`us`, `de`, `cn`, …) | all | Filter by country |
| `anonymity` | `elite`, `anonymous`, `transparent` | all | Filter by anonymity level |
| `ssl` | `strict`, `loose` | all | `strict` = no MITM, valid certificate; `loose` includes invalid-cert proxies |
| `google` | `true` | all | Only proxies that work for Google services |
| `speed` | `fast`, `medium`, `slow` | all | Latency tier |
| `format` | `json`, `csv`, `txt` | `json` | Output format |
| `limit` | `1`–`1000` | `500` | Proxies per page |
| `page` | `1+` | `1` | Page number for pagination |

**Rate limit:** 50 requests / second. Responses are cached for 10 seconds.

### Example Requests

```bash
# All strict-SSL proxies as JSON
curl "https://databay.com/api/v1/proxy-list?ssl=strict"

# Elite SOCKS5 proxies, US only
curl "https://databay.com/api/v1/proxy-list?protocol=socks5&anonymity=elite&country=us&ssl=strict"

# Google-compatible proxies as plain text
curl "https://databay.com/api/v1/proxy-list?google=true&ssl=strict&format=txt"

# Fast proxies as CSV (paginated)
curl "https://databay.com/api/v1/proxy-list?speed=fast&format=csv&limit=100&page=2"
```

### Response Schema

Each proxy record contains:

| Field | Type | Description |
|-------|------|-------------|
| `ip` | string | Proxy IPv4 address |
| `port` | integer | Proxy port |
| `protocol` | string | `http` / `https` / `socks5` |
| `country` | string | ISO 2-letter country code |
| `anonymity` | string | `elite` / `anonymous` / `transparent` |
| `ssl` | string | `strict` / `loose` |
| `google` | boolean | Reachable for Google services |
| `latency_ms` | integer | Last verified latency in ms |
| `uptime` | float | Lifetime uptime % |
| `last_checked` | ISO 8601 | Timestamp of last verification |

---

## 💻 Code Examples

All examples below pull the JSON-formatted strict-SSL list from the API. Drop the API call and use the `.txt` direct downloads if you don't need filtering.

### 🐍 Python

```python
import requests

resp = requests.get(
    "https://databay.com/api/v1/proxy-list",
    params={"ssl": "strict", "protocol": "socks5", "format": "json"},
    timeout=10,
)
proxies = resp.json()

for p in proxies:
    print(f"{p['protocol']}://{p['ip']}:{p['port']}  ({p['country']}, {p['latency_ms']}ms)")
```

Use one with the `requests` library:
```python
proxy = proxies[0]
url_proxy = f"{proxy['protocol']}://{proxy['ip']}:{proxy['port']}"
r = requests.get("https://example.com", proxies={"http": url_proxy, "https": url_proxy})
```

### 🟢 Node.js

```javascript
const res = await fetch(
  "https://databay.com/api/v1/proxy-list?ssl=strict&protocol=socks5"
);
const proxies = await res.json();

for (const p of proxies) {
  console.log(`${p.protocol}://${p.ip}:${p.port}  (${p.country}, ${p.latency_ms}ms)`);
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
    Protocol  string `json:"protocol"`
    Country   string `json:"country"`
    LatencyMs int    `json:"latency_ms"`
}

func main() {
    resp, _ := http.Get("https://databay.com/api/v1/proxy-list?ssl=strict")
    defer resp.Body.Close()

    var proxies []Proxy
    json.NewDecoder(resp.Body).Decode(&proxies)

    for _, p := range proxies {
        fmt.Printf("%s://%s:%d (%s, %dms)\n", p.Protocol, p.IP, p.Port, p.Country, p.LatencyMs)
    }
}
```

### 🐘 PHP

```php
<?php
$json = file_get_contents("https://databay.com/api/v1/proxy-list?ssl=strict");
$proxies = json_decode($json, true);

foreach ($proxies as $p) {
    echo "{$p['protocol']}://{$p['ip']}:{$p['port']} ({$p['country']}, {$p['latency_ms']}ms)\n";
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
// Parse with Jackson, Gson, or any JSON library
```

### 🟣 C# / .NET

```csharp
using System.Net.Http.Json;

var http = new HttpClient();
var proxies = await http.GetFromJsonAsync<List<Proxy>>(
    "https://databay.com/api/v1/proxy-list?ssl=strict&protocol=socks5"
);

foreach (var p in proxies!)
    Console.WriteLine($"{p.Protocol}://{p.Ip}:{p.Port} ({p.Country}, {p.LatencyMs}ms)");

record Proxy(string Ip, int Port, string Protocol, string Country, int LatencyMs);
```

---

## 🛡️ Why Strict SSL Matters

Most "free proxy lists" don't validate that the proxies they ship preserve target SSL certificates. A large fraction of free proxies actively **MITM your HTTPS traffic** — they decrypt it, optionally inject content, and re-encrypt with their own certificate. Apps that disable certificate validation (depressingly common in scrapers) leak credentials and private data straight to the proxy operator.

This list ships **only proxies that have been verified end-to-end against a known target with strict SSL certificate validation enabled**. If a proxy attempts to MITM, it's filtered out before it ever lands in `http.txt` / `socks4.txt` / `socks5.txt`.

For production-grade scraping, browsing, or automation, even strict-SSL free proxies are unreliable (low uptime, shared IPs flagged everywhere). Consider Databay's premium rotating proxies for that workload.

---

## 🚀 Need Premium?

Free proxies are great for testing and one-off jobs, but they share IPs with thousands of other users — meaning they're rate-limited, banned, or blacklisted on most major sites.

[**Databay's premium proxies**](https://databay.com/) give you:

- ✅ **34M+ Residential, Mobile & Datacenter IPs** across 200+ countries
- ✅ **Rotating IPs** — fresh IP per connection
- ✅ **Zero MITM** — fully encrypted HTTPS traffic
- ✅ **Expert support** — direct access to engineers

🔗 [**Get Databay Premium Proxies →**](https://databay.com/)

---

## 📜 License

Released under the [MIT License](LICENSE). Use it freely in personal, commercial, or open-source projects. Attribution appreciated but not required.

---

## ⚠️ Disclaimer

**This proxy list is provided "as-is".** We are not responsible for any misuse or damages. Use at your own risk. Always prioritize security and respect the [GitHub Acceptable Use Policy](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies) and the laws of your jurisdiction.
