// Node.js 22+. Fetches a list; it does not send traffic through a listed proxy.
// Run: node examples/node_fetch.mjs
import { isIPv4 } from "node:net";
import { pathToFileURL } from "node:url";

const API_URL = "https://databay.com/api/v1/proxy-list";
const MAX_BODY_BYTES = 1_000_000;

export async function fetchProxies() {
  const url = new URL(API_URL);
  url.search = new URLSearchParams({ protocol: "socks5", ssl: "strict", limit: "10" });
  const response = await fetch(url, {
    headers: {
      Accept: "application/json",
      "User-Agent": "databay-free-proxy-list-example/1.0 (+https://github.com/databay-labs/free-proxy-list)",
    },
    signal: AbortSignal.timeout(15_000),
  });
  if (!response.ok) {
    await response.body?.cancel();
    throw new Error(`List API returned HTTP ${response.status}.`);
  }

  // Bound the body as well as the request duration.
  const chunks = [];
  let bytes = 0;
  if (response.body) {
    for await (const chunk of response.body) {
      bytes += chunk.byteLength;
      if (bytes > MAX_BODY_BYTES) throw new Error("List response exceeded the 1 MB example limit.");
      chunks.push(chunk);
    }
  }
  const payload = JSON.parse(Buffer.concat(chunks).toString("utf8"));
  if (!payload || !Array.isArray(payload.data)) {
    throw new Error("Expected a JSON object with a data array.");
  }
  for (const proxy of payload.data) {
    if (!proxy || typeof proxy.ip !== "string" || !isIPv4(proxy.ip) ||
        !Number.isInteger(proxy.port) || proxy.port < 1 || proxy.port > 65535 ||
        !String(proxy.protocol ?? "").toLowerCase().split(",").map(x => x.trim()).includes("socks5")) {
      throw new Error("Expected SOCKS5 proxy records with an IPv4 address and valid port.");
    }
  }
  return payload.data;
}

export async function main() {
  try {
    const proxies = await fetchProxies();
    if (proxies.length === 0) {
      console.log("No matching proxies are available. Try again later or change filters.");
      return 0;
    }
    for (const proxy of proxies) console.log(`${proxy.ip}:${proxy.port}`);
    return 0;
  } catch (error) {
    console.error(`Error: ${error.message}`);
    return 1;
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  process.exitCode = await main();
}
