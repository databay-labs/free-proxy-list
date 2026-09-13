# Contributing

Help other developers get a useful result: improve an example, clarify a filter, report a broken feed, or suggest a public source with clear reuse terms.

## Where changes belong

This repository distributes generated proxy lists, documentation, and examples. The scraper service is not included in this repository.

- `README.md`, root proxy `.txt` files, and `by-country/` are generated and replaced during updates. Suggest README wording in a report so maintainers can update the internal publishing template. Do not submit individual proxy additions or removals as edits to generated files.
- Documentation and example pull requests are welcome. Explain the intended behavior and how you checked the change.
- For feed generation, validation, API behavior, or source additions, send a reproducible report using the route below. Maintainers integrate these changes in the publishing source.
- Maintainers must carry accepted templates, documentation, and examples into the publisher's assets so later deployments preserve them. A public-repository edit alone may be overwritten by publishing.

## Report something reproducible

If [GitHub Issues](https://github.com/databay-labs/free-proxy-list/issues) is enabled, search existing reports first, then use the bug or feature template. Otherwise, email the maintainers at [hello@databay.com](mailto:hello@databay.com). For a feed/API report, include the exact URL and filters, UTC observation time, HTTP status, and a small sanitized response or command. For a GitHub feed, include the commit ID when available.

One endpoint failing later is normal for public proxies. A useful bug report identifies a repeatable problem, such as malformed lines, an unavailable download, an incorrect filter, or an example that fails before a proxy is used. Never include credentials, session cookies, or private destination URLs.

## Check documentation and examples

Keep examples small, set network timeouts, handle HTTP errors and empty lists, and leave TLS certificate verification enabled. Check Python syntax with `python -B -c "import ast, pathlib; ast.parse(pathlib.Path('examples/python_requests.py').read_text())"` and JavaScript syntax with `node --check examples/node_fetch.mjs`. You can test response parsing with fixtures; testing real public proxies is not required for a documentation contribution.

Preserve [LICENSE](LICENSE) when reusing or changing this repository's material. For a proposed new source, link to its public feed and its license or permission to redistribute; do not submit private or authenticated feeds.
