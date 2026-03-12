<h1 align="center">PassXAPI Python SDK</h1>

<p align="center">
  <b>Official Python SDK for <a href="https://passxapi.com">PassXAPI</a> captcha & anti-bot solving service</b>
</p>

<p align="center">
  <a href="https://pypi.org/project/passxapi/"><img src="https://img.shields.io/pypi/v/passxapi?color=blue" alt="PyPI"></a>
  <a href="https://pypi.org/project/passxapi/"><img src="https://img.shields.io/pypi/pyversions/passxapi" alt="Python"></a>
  <a href="https://github.com/passxapi/passxapi-python/blob/main/LICENSE"><img src="https://img.shields.io/github/license/passxapi/passxapi-python" alt="License"></a>
  <a href="https://passxapi.com/docs"><img src="https://img.shields.io/badge/docs-API%20Reference-green" alt="Docs"></a>
</p>

<p align="center">
  <a href="https://github.com/passxapi/passxapi-python">Python</a> ·
  <a href="https://github.com/passxapi/passxapi-node">Node.js</a> ·
  <a href="https://passxapi.com/docs">API Docs</a> ·
  <a href="https://passxapi.com/services">Pricing</a> ·
  <a href="https://github.com/passxapi/passxapi-python/blob/main/README_zh.md">中文文档</a>
</p>

---

## Supported CAPTCHA Types

| Type | Method | Avg. Time | Sites |
|------|--------|-----------|-------|
| [reCAPTCHA v3](#recaptcha-v3) | `recaptcha_v3()` | 8-15s | Google, YouTube, LinkedIn, Steam, PayPal |
| [hCaptcha](#hcaptcha) | `hcaptcha()` | 5-12s | Cloudflare, Discord, Epic Games, Coinbase |
| [hCaptcha Pro](#hcaptcha-pro) | `hcaptcha_pro()` | 8-15s | Cloudflare Enterprise, Binance, Kraken |
| [Cloudflare Turnstile](#cloudflare-turnstile) | `cloudflare_turnstile()` | 3-8s | DHL, Notion, Canva, Vercel, GitLab, Figma |
| [Cloudflare WAF](#cloudflare-waf) | `cloudflare_waf()` | 5-10s | Shopify, Medium, Discord, OpenAI |
| [Akamai Bot Manager](#akamai) | `akamai()` | 5-15s | Nike, Adidas, United Airlines, Walmart |
| [Akamai sec_cpt](#akamai-sec_cpt) | `akamai_sec_cpt()` | 5-15s | Nike, Ticketmaster, Best Buy, Nordstrom |
| [PerimeterX Silent](#perimeterx) | `perimeterx_silent()` | 5-12s | Zillow, Craigslist, Indeed, StockX |
| [PerimeterX Challenge](#perimeterx) | `perimeterx_challenge()` | 8-15s | Zillow, Wayfair, Glassdoor, Redfin |
| [Kasada ct](#kasada) | `kasada_ct()` | 5-12s | Kick, bet365, DraftKings, PlayStation |
| [Kasada cd](#kasada) | `kasada_cd()` | 5-12s | Kick, bet365, FanDuel, Canada Goose |
| [Kasada TL Payload](#kasada) | `kasada_tl_payload()` | 5-10s | Kick, bet365, DraftKings, Twitch |
| [DataDome Silent](#datadome) | `datadome_silent()` | 5-12s | Reddit, SoundCloud, TripAdvisor, Vinted |
| [DataDome Invisible](#datadome) | `datadome_invisible()` | 5-12s | Reddit, Rakuten, AllTrails, Foot Locker EU |
| [DataDome Slider](#datadome) | `datadome_slider()` | 5-15s | Reddit, Leboncoin, Hermes, TripAdvisor |
| [Shape Security](#shape-security) | `shape()` | 8-20s | Southwest Airlines, Starbucks, Citibank |
| [FunCaptcha](#funcaptcha) | `funcaptcha()` | 8-15s | Microsoft, Roblox, GitHub, Snapchat, X |
| [AWS WAF](#aws-waf) | `aws()` | 5-12s | Amazon, Twitch, IMDb, Audible, Zappos |
| [Vercel Challenge](#vercel-challenge) | `vercel_challenge()` | 3-8s | TikTok Web, Hashnode, Cal.com, Loom |
| [Castle](#castle) | `castle()` | 5-10s | Carta, Plaid, Mercury, Brex, Notion |
| [Reese84](#reese84) | `reese84()` | 5-15s | Glassdoor, Western Union, HSBC, Siemens |
| [UTMVC](#utmvc) | `utmvc()` | 5-15s | Glassdoor, Indeed, Kroger, AutoTrader |
| [Sbsd](#sbsd) | `sbsd()` | 5-12s | Ticketmaster, StubHub, SeatGeek, AXS |
| [CaptchaFox](#captchafox) | `captchafox()` | 3-8s | Zalando, Otto, Booking.com, BMW |
| [Forter](#forter) | `forter()` | 5-12s | Nordstrom, Instacart, Sephora, Uber Eats |
| [ThreatMetrix](#threatmetrix) | `threatmetrix()` | 5-15s | Chase, Wells Fargo, PayPal, Robinhood |
| [TLS Forward](#tls-forward) | `tls_forward()` | 3-8s | Any site with JA3/JA4 fingerprint detection |

> **27 types supported** · Failed requests are **never charged** · Avg success rate **99.5%+**

---

## Why PassXAPI?

| | PassXAPI | 2Captcha | CapSolver |
|---|:---:|:---:|:---:|
| **Price per solve** | **$0.001** | $0.003 | $0.002 |
| Captcha types | **27** | ~15 | ~12 |
| Akamai / PerimeterX / Kasada | ✅ | ❌ | ❌ |
| Shape / Forter / ThreatMetrix | ✅ | ❌ | ❌ |
| TLS fingerprint forwarding | ✅ | ❌ | ❌ |
| Webhook callback | ✅ | ❌ | ❌ |
| Failed = free | ✅ | ❌ | ❌ |

---

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Solve CAPTCHA](#solve-captcha)
  - [reCAPTCHA v3](#recaptcha-v3)
  - [hCaptcha](#hcaptcha)
  - [hCaptcha Pro](#hcaptcha-pro)
  - [Cloudflare Turnstile](#cloudflare-turnstile)
  - [Cloudflare WAF](#cloudflare-waf)
  - [Akamai](#akamai)
  - [Akamai sec_cpt](#akamai-sec_cpt)
  - [PerimeterX](#perimeterx)
  - [Kasada](#kasada)
  - [DataDome](#datadome)
  - [Shape Security](#shape-security)
  - [FunCaptcha](#funcaptcha)
  - [AWS WAF](#aws-waf)
  - [Vercel Challenge](#vercel-challenge)
  - [Castle](#castle)
  - [Reese84](#reese84)
  - [UTMVC](#utmvc)
  - [Sbsd](#sbsd)
  - [CaptchaFox](#captchafox)
  - [Forter](#forter)
  - [ThreatMetrix](#threatmetrix)
  - [TLS Forward](#tls-forward)
- [Webhook Callback](#webhook-callback)
- [Account & Billing](#account--billing)
- [Configuration](#configuration)
- [Error Handling](#error-handling)
- [Low-Level API](#low-level-api)
- [Migration from 2Captcha](#migration-from-2captcha)
- [Links](#links)

---

## Installation

```bash
pip install passxapi
```

Requires Python 3.7+. Only dependency: `requests`.

## Quick Start

```python
from passxapi import PassXAPI

client = PassXAPI("YOUR_API_KEY")

result = client.cloudflare_turnstile(
    target_url="https://example.com",
    proxy="http://user:pass@ip:port",
    site_key="0x4AAAAAAA...",
)

print(result["token"])       # Verification token
print(result["cookies"])     # {"cf_clearance": "..."}
print(result["ua"])          # User-Agent string to use
```

1. [Sign up](https://passxapi.com/login) — free, no credit card
2. [Create API key](https://passxapi.com/app/api-keys)
3. `pip install passxapi`

---

## Solve CAPTCHA

All methods follow the same pattern: **submit → poll → return result**. The SDK handles polling automatically.

- **Proxy required** for all methods. Format: `http://user:pass@ip:port` (residential recommended)
- **Result** is a dict containing `token`, and optionally `cookies` and `ua`

---

### reCAPTCHA v3

> Google, YouTube, LinkedIn, Steam, PayPal, Binance · [API docs →](https://passxapi.com/docs)

```python
result = client.recaptcha_v3(
    target_url="https://example.com",
    proxy="http://user:pass@ip:port",
    site_key="6Le-wvkSAAAA...",
    action="login",          # Action parameter
    enterprise=False,        # Set True for Enterprise
    title="Page Title",      # Optional
)
```

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `target_url` | ✅ | Page URL with reCAPTCHA |
| `proxy` | ✅ | HTTP proxy string |
| `site_key` | ✅ | Google site key |
| `action` | ❌ | Action parameter (default: `"verify"`) |
| `enterprise` | ❌ | Enterprise version (default: `False`) |
| `title` | ❌ | Page title |

---

### hCaptcha

> Cloudflare, Discord, Epic Games, Coinbase, NordVPN · [API docs →](https://passxapi.com/docs)

```python
result = client.hcaptcha(
    target_url="https://example.com",
    proxy="http://user:pass@ip:port",
    site_key="SITE_KEY",
)
```

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `target_url` | ✅ | Page URL |
| `proxy` | ✅ | HTTP proxy |
| `site_key` | ✅ | hCaptcha site key |

---

### hCaptcha Pro

> Cloudflare Enterprise, Coinbase, Binance, Kraken · [API docs →](https://passxapi.com/docs)

```python
result = client.hcaptcha_pro(
    target_url="https://example.com",
    proxy="http://user:pass@ip:port",
)
```

---

### Cloudflare Turnstile

> DHL, Notion, Canva, Vercel, GitLab, Figma, HubSpot · [API docs →](https://passxapi.com/docs)

```python
result = client.cloudflare_turnstile(
    target_url="https://example.com",
    proxy="http://user:pass@ip:port",
    site_key="0x4AAAAAAA...",
)
```

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `target_url` | ✅ | Page URL |
| `proxy` | ✅ | HTTP proxy |
| `site_key` | ✅ | Turnstile site key |

---

### Cloudflare WAF

> Shopify, Medium, Discord, OpenAI, Notion, Figma · [API docs →](https://passxapi.com/docs)

```python
result = client.cloudflare_waf(
    target_url="https://example.com",
    proxy="http://user:pass@ip:port",
    target_method="GET",     # HTTP method (GET/POST)
)
```

---

### Akamai

> Nike, Adidas, Delta Airlines, Walmart, Costco, Airbnb · [API docs →](https://passxapi.com/docs)

```python
result = client.akamai(
    target_url="https://nike.com",
    proxy="http://user:pass@ip:port",
    akamai_js_url="https://nike.com/_sec/cp_challenge/ak-challenge-xxx.js",
    page_fp="abc123",        # Optional: page fingerprint
)
```

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `target_url` | ✅ | Page URL |
| `proxy` | ✅ | HTTP proxy |
| `akamai_js_url` | ✅ | Akamai challenge JS URL |
| `page_fp` | ❌ | Page fingerprint value |

---

### Akamai sec_cpt

> Nike, Adidas, Ticketmaster, Best Buy, Nordstrom · [API docs →](https://passxapi.com/docs)

```python
result = client.akamai_sec_cpt(
    target_url="https://nike.com",
    proxy="http://user:pass@ip:port",
    sec_cpt="challenge_token",
    sec_json={
        "nonce": "...",
        "difficulty": 5,
        "token": "...",
        "count": 0,
        "timestamp": 1234567890,
    },
)
```

---

### PerimeterX

> Zillow, Craigslist, Indeed, StockX, Wayfair, Reddit · [API docs →](https://passxapi.com/docs)

**Silent** (no visual challenge):
```python
result = client.perimeterx_silent(
    target_url="https://zillow.com",
    proxy="http://user:pass@ip:port",
    perimeterx_js_url="https://client.px-cdn.net/PX.../main.min.js",
    pxAppId="PX...",
)
```

**Interactive challenge**:
```python
result = client.perimeterx_challenge(
    target_url="https://zillow.com",
    proxy="http://user:pass@ip:port",
    pxvid="...",
    pxuuid="...",
    pxAppId="PX...",
    perimeterx_js_url="...",
    captcha_js_url="...",
    init_cookies={"pxhd": "..."},
)
```

---

### Kasada

> Kick, bet365, DraftKings, FanDuel, PlayStation, Twitch · [API docs →](https://passxapi.com/docs)

**ct**:
```python
result = client.kasada_ct(
    target_url="https://kick.com",
    proxy="http://user:pass@ip:port",
    protected_api_domain="kick.com",
    kasada_js_domain="k.tl",
)
```

**cd** (advanced):
```python
result = client.kasada_cd(
    target_url="https://kick.com",
    proxy="http://user:pass@ip:port",
    ct="...", st="...", fc="...", site="kick.com",
)
```

**TL Payload**:
```python
result = client.kasada_tl_payload(
    target_url="https://kick.com",
    proxy="http://user:pass@ip:port",
)
```

---

### DataDome

> Reddit, SoundCloud, Rakuten, TripAdvisor, Vinted, Hermes · [API docs →](https://passxapi.com/docs)

**Silent**:
```python
result = client.datadome_silent(
    target_url="https://reddit.com",
    proxy="http://user:pass@ip:port",
    target_method="GET",
)
```

**Invisible**:
```python
result = client.datadome_invisible(
    target_url="https://reddit.com",
    proxy="http://user:pass@ip:port",
    datadome_js_url="https://js.datadome.co/tags.js",
    ddjskey="ABCDEF123",
    ddoptions='{"ajaxListenerPath":"..."}',
)
```

**Slider**:
```python
result = client.datadome_slider(
    target_url="https://reddit.com",
    proxy="http://user:pass@ip:port",
    target_method="GET",
    init_cookies={"datadome": "..."},
)
```

---

### Shape Security

> Southwest Airlines, Starbucks, Citibank, Capital One, Macy's · [API docs →](https://passxapi.com/docs)

```python
result = client.shape(
    target_url="https://southwest.com",
    proxy="http://user:pass@ip:port",
    target_api="https://southwest.com/api/air-booking/...",
    shape_js_url="https://southwest.com/.../shape.js",
    method="POST",
    title="Page Title",      # Optional
)
```

---

### FunCaptcha

> Microsoft, Roblox, GitHub, Snapchat, LinkedIn, Adobe, X · [API docs →](https://passxapi.com/docs)

```python
result = client.funcaptcha(
    target_url="https://outlook.com",
    proxy="http://user:pass@ip:port",
    public_key="B7D8911C-5CC8-A9A3-...",
    custom_api_host="client-api.arkoselabs.com",  # Optional
)
```

---

### AWS WAF

> Amazon, Twitch, IMDb, Audible, Zappos · [API docs →](https://passxapi.com/docs)

```python
result = client.aws(
    target_url="https://amazon.com",
    proxy="http://user:pass@ip:port",
    aws_js_url="https://xxx.token.awswaf.com/xxx/challenge.js",
)
```

---

### Vercel Challenge

> TikTok Web, Hashnode, Cal.com, Loom, Neon · [API docs →](https://passxapi.com/docs)

```python
result = client.vercel_challenge(
    target_url="https://example.vercel.app",
    proxy="http://user:pass@ip:port",
)
```

---

### Castle

> Carta, Gusto, Plaid, Mercury, Brex, Notion · [API docs →](https://passxapi.com/docs)

```python
result = client.castle(
    target_url="https://example.com",
    proxy="http://user:pass@ip:port",
    config_json={"pk": "pk_xxx", "avoidCookies": False},
)
# Returns "request_token" instead of "token"
```

---

### Reese84

> Glassdoor, Western Union, HSBC, Singapore Airlines · [API docs →](https://passxapi.com/docs)

```python
result = client.reese84(
    target_url="https://glassdoor.com",
    proxy="http://user:pass@ip:port",
    reese84_js_url="https://glassdoor.com/.../reese84.js",
)
```

---

### UTMVC

> Glassdoor, Indeed, Kroger, AutoTrader, TripAdvisor · [API docs →](https://passxapi.com/docs)

```python
result = client.utmvc(
    target_url="https://indeed.com",
    proxy="http://user:pass@ip:port",
    utmvc_js_url="https://indeed.com/.../incapsula.js",
    incap_cookie={
        "visid_incap_xxx": "...",
        "nlbi_xxx": "...",
        "incap_ses_xxx": "...",
    },
)
```

---

### Sbsd

> Ticketmaster, StubHub, Vivid Seats, SeatGeek, AXS · [API docs →](https://passxapi.com/docs)

```python
result = client.sbsd(
    target_url="https://ticketmaster.com",
    proxy="http://user:pass@ip:port",
    sbsd_js_url="https://ticketmaster.com/.../bot-manager.js",
    init_cookies={"bm_s": "...", "bm_sc": "..."},
)
```

---

### CaptchaFox

> Zalando, Otto, Booking.com, BMW, Deutsche Telekom · [API docs →](https://passxapi.com/docs)

```python
result = client.captchafox(
    target_url="https://example.de",
    proxy="http://user:pass@ip:port",
    site_key="sk-xxx",
)
```

---

### Forter

> Nordstrom, Instacart, Sephora, Lululemon, Uber Eats · [API docs →](https://passxapi.com/docs)

```python
result = client.forter(
    target_url="https://nordstrom.com",
    proxy="http://user:pass@ip:port",
    forter_js_url="https://cdn4.forter.com/xxx.js",
    site_id="xxx",
)
```

---

### ThreatMetrix

> Chase, Wells Fargo, Bank of America, PayPal, Robinhood · [API docs →](https://passxapi.com/docs)

```python
result = client.threatmetrix(
    target_url="https://chase.com",
    proxy="http://user:pass@ip:port",
    org_id="xxx",
    page_id="xxx",
    session_id="xxx",
    custom_domain="h.online-metrix.net",
    title="Page Title",      # Optional
)
```

---

### TLS Forward

> Any site with JA3/JA4 fingerprint detection · [API docs →](https://passxapi.com/docs)

```python
result = client.tls_forward(
    target_url="https://example.com",
    proxy="http://user:pass@ip:port",
)
```

---

## Webhook Callback

Instead of polling, receive results via webhook:

```python
task_id = client.submit(
    task_type="cloudflare_turnstile",
    proxy="http://user:pass@ip:port",
    target_url="https://example.com",
    site_key="0x4AAAAAAA...",
    callback_url="https://your-server.com/webhook",
)
```

Your server receives:

```json
{
    "taskId": "abc123-def456",
    "status": "ready",
    "errorId": 0,
    "solution": {
        "token": "P0_eyJ...",
        "cookies": {"cf_clearance": "xxx"},
        "userAgent": "Mozilla/5.0..."
    }
}
```

Retry policy: up to 3 retries at 5s, 30s, 120s intervals if HTTP 200 is not returned.

---

## Account & Billing

```python
# Check balance
balance = client.get_balance()
print(f"${balance}")

# API key info (status, limits, today's spend)
info = client.get_key_info()
print(f"Key: {info['keyPrefix']}...")
print(f"Active: {info['isActive']}")
print(f"Today: ${info['todaySpent']}")
print(f"Daily limit: {info['dailySpendLimit'] or 'unlimited'}")

# Spending stats (by day, by type)
stats = client.get_spending_stats()
stats = client.get_spending_stats(queue="cloudflare_turnstile")

# Pricing (no auth required)
for p in client.get_pricing():
    print(f"{p['name']}: ${p['price_per_solve']}/solve, "
          f"~{p['avg_solve_time']}s, {p['success_rate']}%")
```

---

## Configuration

```python
client = PassXAPI(
    api_key="YOUR_API_KEY",
    polling_interval=1.5,  # Seconds between polls (default: 1.5)
    timeout=120.0,         # Max wait in seconds (default: 120)
)
```

---

## Error Handling

```python
from passxapi import (
    PassXAPI,
    AuthError,
    ZeroBalanceError,
    CaptchaUnsolvableError,
    BadParametersError,
)

try:
    result = client.cloudflare_turnstile(...)
except AuthError:
    print("Invalid API key")
except ZeroBalanceError:
    print("Top up at https://passxapi.com/app/billing/deposit")
except CaptchaUnsolvableError:
    print("Could not solve")
except BadParametersError as e:
    print(f"Bad params: {e}")
```

| Exception | Error Code | When |
|-----------|-----------|------|
| `AuthError` | `ERROR_AUTH` | Invalid API key |
| `ZeroBalanceError` | `ERROR_ZERO_BALANCE` | Insufficient balance |
| `BadParametersError` | `ERROR_BAD_PARAMETERS` | Missing or invalid params |
| `CaptchaUnsolvableError` | `ERROR_CAPTCHA_UNSOLVABLE` | Failed to solve / timeout |
| `TaskNotFoundError` | `ERROR_NO_SUCH_CAPCHA_ID` | Task ID not found |
| `RateLimitError` | `ERROR_RATE_LIMIT` | Concurrency limit exceeded |
| `DailyLimitError` | `ERROR_DAILY_LIMIT_REACHED` | Daily spend limit hit |
| `IPNotAllowedError` | `ERROR_IP_NOT_ALLOWED` | IP not in whitelist |

> Failed requests are **never charged**.

---

## Low-Level API

```python
# Submit task manually
task_id = client.submit(
    task_type="cloudflare_turnstile",
    proxy="http://user:pass@ip:port",
    target_url="https://example.com",
    site_key="0x4AAAAAAA...",
)

# Poll for result
import time
while True:
    result = client.get_result(task_id)
    if result["status"] == "SUCCESS":
        print(result["result"]["token"])
        break
    time.sleep(1.5)
```

---

## Migration from 2Captcha

```diff
- from twocaptcha import TwoCaptcha
- solver = TwoCaptcha("API_KEY")
- result = solver.recaptcha(sitekey="KEY", url="https://example.com")

+ from passxapi import PassXAPI
+ solver = PassXAPI("API_KEY")
+ result = solver.recaptcha_v3(
+     target_url="https://example.com",
+     proxy="http://user:pass@ip:port",
+     site_key="KEY",
+ )
```

---

## Links

| | |
|---|---|
| **Website** | https://passxapi.com |
| **Sign Up** | https://passxapi.com/login |
| **API Keys** | https://passxapi.com/app/api-keys |
| **API Docs** | https://passxapi.com/docs |
| **Dashboard** | https://passxapi.com/app/dashboard |
| **Pricing** | https://passxapi.com/services |
| **Support** | contact@passxapi.com |

## License

[MIT](LICENSE) © PassXAPI
