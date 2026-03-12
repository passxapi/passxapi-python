<h1 align="center">PassXAPI Python SDK</h1>

<p align="center">
  <b><a href="https://www.passxapi.com">PassXAPI</a> 官方 Python SDK — 验证码 & 反机器人自动化解决方案</b>
</p>

<p align="center">
  <a href="https://pypi.org/project/passxapi/"><img src="https://img.shields.io/pypi/v/passxapi?color=blue" alt="PyPI"></a>
  <a href="https://pypi.org/project/passxapi/"><img src="https://img.shields.io/pypi/pyversions/passxapi" alt="Python"></a>
  <a href="https://github.com/passxapi/passxapi-python/blob/main/LICENSE"><img src="https://img.shields.io/github/license/passxapi/passxapi-python" alt="License"></a>
  <a href="https://www.passxapi.com/docs"><img src="https://img.shields.io/badge/docs-API%20Reference-green" alt="Docs"></a>
</p>

<p align="center">
  <a href="https://github.com/passxapi/passxapi-python/blob/main/README.md">English</a> ·
  <b>中文</b> ·
  <a href="https://www.passxapi.com/docs">API 文档</a> ·
  <a href="https://www.passxapi.com/services">价格</a>
</p>

---

## 支持的验证码类型

| 类型 | 方法 | 平均耗时 | 常见网站 |
|------|------|----------|---------|
| [reCAPTCHA v3](#recaptcha-v3) | `recaptcha_v3()` | 8-15秒 | Google, YouTube, LinkedIn, Steam, PayPal |
| [hCaptcha](#hcaptcha) | `hcaptcha()` | 5-12秒 | Cloudflare, Discord, Epic Games, Coinbase |
| [hCaptcha Pro](#hcaptcha-pro) | `hcaptcha_pro()` | 8-15秒 | Cloudflare Enterprise, Binance, Kraken |
| [Cloudflare Turnstile](#cloudflare-turnstile) | `cloudflare_turnstile()` | 3-8秒 | DHL, Notion, Canva, Vercel, GitLab, Figma |
| [Cloudflare WAF](#cloudflare-waf) | `cloudflare_waf()` | 5-10秒 | Shopify, Medium, Discord, OpenAI |
| [Akamai Bot Manager](#akamai) | `akamai()` | 5-15秒 | Nike, Adidas, United Airlines, Walmart |
| [Akamai sec_cpt](#akamai-sec_cpt) | `akamai_sec_cpt()` | 5-15秒 | Nike, Ticketmaster, Best Buy, Nordstrom |
| [PerimeterX Silent](#perimeterx) | `perimeterx_silent()` | 5-12秒 | Zillow, Craigslist, Indeed, StockX |
| [PerimeterX Challenge](#perimeterx) | `perimeterx_challenge()` | 8-15秒 | Zillow, Wayfair, Glassdoor, Redfin |
| [Kasada ct](#kasada) | `kasada_ct()` | 5-12秒 | Kick, bet365, DraftKings, PlayStation |
| [Kasada cd](#kasada) | `kasada_cd()` | 5-12秒 | Kick, bet365, FanDuel, Canada Goose |
| [Kasada TL Payload](#kasada) | `kasada_tl_payload()` | 5-10秒 | Kick, bet365, DraftKings, Twitch |
| [DataDome Silent](#datadome) | `datadome_silent()` | 5-12秒 | Reddit, SoundCloud, TripAdvisor, Vinted |
| [DataDome Invisible](#datadome) | `datadome_invisible()` | 5-12秒 | Reddit, Rakuten, AllTrails, Foot Locker EU |
| [DataDome Slider](#datadome) | `datadome_slider()` | 5-15秒 | Reddit, Leboncoin, Hermes, TripAdvisor |
| [Shape Security](#shape-security) | `shape()` | 8-20秒 | Southwest Airlines, Starbucks, Citibank |
| [FunCaptcha](#funcaptcha) | `funcaptcha()` | 8-15秒 | Microsoft, Roblox, GitHub, Snapchat, X |
| [AWS WAF](#aws-waf) | `aws()` | 5-12秒 | Amazon, Twitch, IMDb, Audible, Zappos |
| [Vercel Challenge](#vercel-challenge) | `vercel_challenge()` | 3-8秒 | TikTok Web, Hashnode, Cal.com, Loom |
| [Castle](#castle) | `castle()` | 5-10秒 | Carta, Plaid, Mercury, Brex, Notion |
| [Reese84](#reese84) | `reese84()` | 5-15秒 | Glassdoor, Western Union, HSBC, Siemens |
| [UTMVC](#utmvc) | `utmvc()` | 5-15秒 | Glassdoor, Indeed, Kroger, AutoTrader |
| [Sbsd](#sbsd) | `sbsd()` | 5-12秒 | Ticketmaster, StubHub, SeatGeek, AXS |
| [CaptchaFox](#captchafox) | `captchafox()` | 3-8秒 | Zalando, Otto, Booking.com, BMW |
| [Forter](#forter) | `forter()` | 5-12秒 | Nordstrom, Instacart, Sephora, Uber Eats |
| [ThreatMetrix](#threatmetrix) | `threatmetrix()` | 5-15秒 | Chase, Wells Fargo, PayPal, Robinhood |
| [TLS Forward](#tls-forward) | `tls_forward()` | 3-8秒 | 任何使用 JA3/JA4 指纹检测的网站 |

> **支持 27 种验证码类型** · 失败请求**不收费** · 平均成功率 **99.5%+**

---

## 为什么选择 PassXAPI？

| | PassXAPI | 2Captcha | CapSolver |
|---|:---:|:---:|:---:|
| **单次价格** | **$0.001** | $0.003 | $0.002 |
| 验证码类型 | **27** | ~15 | ~12 |
| Akamai / PerimeterX / Kasada | ✅ | ❌ | ❌ |
| Shape / Forter / ThreatMetrix | ✅ | ❌ | ❌ |
| TLS 指纹转发 | ✅ | ❌ | ❌ |
| Webhook 回调 | ✅ | ❌ | ❌ |
| 失败不收费 | ✅ | ❌ | ❌ |

---

## 目录

- [安装](#安装)
- [快速开始](#快速开始)
- [验证码求解](#验证码求解)
  - [reCAPTCHA v3](#recaptcha-v3)
  - [hCaptcha](#hcaptcha)
  - [hCaptcha Pro](#hcaptcha-pro)
  - [Cloudflare Turnstile](#cloudflare-turnstile)
  - [Cloudflare WAF](#cloudflare-waf)
  - [Akamai](#akamai)
  - [PerimeterX](#perimeterx)
  - [Kasada](#kasada)
  - [DataDome](#datadome)
  - [Shape Security](#shape-security)
  - [FunCaptcha](#funcaptcha)
  - [AWS WAF](#aws-waf)
  - [其他类型](#其他类型)
- [Webhook 回调](#webhook-回调)
- [账户与计费](#账户与计费)
- [配置](#配置)
- [错误处理](#错误处理)
- [底层 API](#底层-api)
- [从 2Captcha 迁移](#从-2captcha-迁移)
- [相关链接](#相关链接)

---

## 安装

```bash
pip install passxapi
```

要求 Python 3.7+，唯一依赖：`requests`。

## 快速开始

```python
from passxapi import PassXAPI

client = PassXAPI("YOUR_API_KEY")

result = client.cloudflare_turnstile(
    target_url="https://example.com",
    proxy="http://user:pass@ip:port",
    site_key="0x4AAAAAAA...",
)

print(result["token"])       # 验证 token
print(result["cookies"])     # {"cf_clearance": "..."}
print(result["ua"])          # 需要使用的 User-Agent
```

1. [注册账号](https://www.passxapi.com/login) — 免费，无需信用卡
2. [创建 API Key](https://www.passxapi.com/app/api-keys)
3. `pip install passxapi`

---

## 验证码求解

所有方法遵循相同模式：**提交 → 轮询 → 返回结果**。SDK 自动处理轮询。

- **代理必填**，格式：`http://user:pass@ip:port`（推荐住宅代理）
- **返回值**为 dict，包含 `token`，以及可选的 `cookies` 和 `ua`

---

### reCAPTCHA v3

> Google, YouTube, LinkedIn, Steam, PayPal, Binance · [API 文档 →](https://www.passxapi.com/docs)

```python
result = client.recaptcha_v3(
    target_url="https://example.com",
    proxy="http://user:pass@ip:port",
    site_key="6Le-wvkSAAAA...",
    action="login",          # action 参数
    enterprise=False,        # Enterprise 版本设为 True
    title="页面标题",         # 可选
)
```

| 参数 | 必填 | 说明 |
|------|:----:|------|
| `target_url` | ✅ | 含 reCAPTCHA 的页面 URL |
| `proxy` | ✅ | HTTP 代理 |
| `site_key` | ✅ | Google site key |
| `action` | ❌ | action 参数（默认 `"verify"`） |
| `enterprise` | ❌ | 是否 Enterprise 版（默认 `False`） |
| `title` | ❌ | 页面标题 |

---

### hCaptcha

> Cloudflare, Discord, Epic Games, Coinbase, NordVPN · [API 文档 →](https://www.passxapi.com/docs)

```python
result = client.hcaptcha(
    target_url="https://example.com",
    proxy="http://user:pass@ip:port",
    site_key="SITE_KEY",
)
```

---

### hCaptcha Pro

> Cloudflare Enterprise, Coinbase, Binance, Kraken · [API 文档 →](https://www.passxapi.com/docs)

```python
result = client.hcaptcha_pro(
    target_url="https://example.com",
    proxy="http://user:pass@ip:port",
)
```

---

### Cloudflare Turnstile

> DHL, Notion, Canva, Vercel, GitLab, Figma, HubSpot · [API 文档 →](https://www.passxapi.com/docs)

```python
result = client.cloudflare_turnstile(
    target_url="https://example.com",
    proxy="http://user:pass@ip:port",
    site_key="0x4AAAAAAA...",
)
```

---

### Cloudflare WAF

> Shopify, Medium, Discord, OpenAI, Notion, Figma · [API 文档 →](https://www.passxapi.com/docs)

```python
result = client.cloudflare_waf(
    target_url="https://example.com",
    proxy="http://user:pass@ip:port",
    target_method="GET",     # HTTP 方法 (GET/POST)
)
```

---

### Akamai

> Nike, Adidas, Delta Airlines, Walmart, Costco, Airbnb · [API 文档 →](https://www.passxapi.com/docs)

```python
result = client.akamai(
    target_url="https://nike.com",
    proxy="http://user:pass@ip:port",
    akamai_js_url="https://nike.com/_sec/cp_challenge/ak-challenge-xxx.js",
    page_fp="abc123",        # 可选：页面指纹
)
```

---

### PerimeterX

> Zillow, Craigslist, Indeed, StockX, Wayfair, Reddit · [API 文档 →](https://www.passxapi.com/docs)

**静默模式**（无可视验证）：
```python
result = client.perimeterx_silent(
    target_url="https://zillow.com",
    proxy="http://user:pass@ip:port",
    perimeterx_js_url="https://client.px-cdn.net/PX.../main.min.js",
    pxAppId="PX...",
)
```

**交互式验证**：
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

> Kick, bet365, DraftKings, FanDuel, PlayStation, Twitch · [API 文档 →](https://www.passxapi.com/docs)

```python
# ct 模式
result = client.kasada_ct(
    target_url="https://kick.com",
    proxy="http://user:pass@ip:port",
    protected_api_domain="kick.com",
    kasada_js_domain="k.tl",
)

# cd 模式（高级）
result = client.kasada_cd(
    target_url="https://kick.com",
    proxy="http://user:pass@ip:port",
    ct="...", st="...", fc="...", site="kick.com",
)

# TL Payload
result = client.kasada_tl_payload(
    target_url="https://kick.com",
    proxy="http://user:pass@ip:port",
)
```

---

### DataDome

> Reddit, SoundCloud, Rakuten, TripAdvisor, Vinted, Hermes · [API 文档 →](https://www.passxapi.com/docs)

```python
# 静默模式
result = client.datadome_silent(
    target_url="https://reddit.com",
    proxy="http://user:pass@ip:port",
    target_method="GET",
)

# 不可见模式
result = client.datadome_invisible(
    target_url="https://reddit.com",
    proxy="http://user:pass@ip:port",
    datadome_js_url="https://js.datadome.co/tags.js",
    ddjskey="ABCDEF123",
    ddoptions='{"ajaxListenerPath":"..."}',
)

# 滑块验证
result = client.datadome_slider(
    target_url="https://reddit.com",
    proxy="http://user:pass@ip:port",
    target_method="GET",
    init_cookies={"datadome": "..."},
)
```

---

### Shape Security

> Southwest Airlines, Starbucks, Citibank, Capital One, Macy's · [API 文档 →](https://www.passxapi.com/docs)

```python
result = client.shape(
    target_url="https://southwest.com",
    proxy="http://user:pass@ip:port",
    target_api="https://southwest.com/api/air-booking/...",
    shape_js_url="https://southwest.com/.../shape.js",
    method="POST",
)
```

---

### FunCaptcha

> Microsoft, Roblox, GitHub, Snapchat, LinkedIn, Adobe, X · [API 文档 →](https://www.passxapi.com/docs)

```python
result = client.funcaptcha(
    target_url="https://outlook.com",
    proxy="http://user:pass@ip:port",
    public_key="B7D8911C-5CC8-A9A3-...",
    custom_api_host="client-api.arkoselabs.com",  # 可选
)
```

---

### AWS WAF

> Amazon, Twitch, IMDb, Audible, Zappos · [API 文档 →](https://www.passxapi.com/docs)

```python
result = client.aws(
    target_url="https://amazon.com",
    proxy="http://user:pass@ip:port",
    aws_js_url="https://xxx.token.awswaf.com/xxx/challenge.js",
)
```

---

### 其他类型

SDK 还支持以下类型，用法类似：

- **Vercel Challenge** — `vercel_challenge()` — TikTok Web, Hashnode, Cal.com
- **Castle** — `castle()` — Carta, Plaid, Mercury, Brex
- **Reese84** — `reese84()` — Glassdoor, Western Union, HSBC
- **UTMVC** — `utmvc()` — Glassdoor, Indeed, Kroger
- **Sbsd** — `sbsd()` — Ticketmaster, StubHub, SeatGeek
- **CaptchaFox** — `captchafox()` — Zalando, Otto, Booking.com
- **Forter** — `forter()` — Nordstrom, Instacart, Sephora
- **ThreatMetrix** — `threatmetrix()` — Chase, Wells Fargo, PayPal
- **TLS Forward** — `tls_forward()` — 任何 JA3/JA4 指纹检测站点

完整参数请参考 [英文文档](README.md) 或 [API 文档](https://www.passxapi.com/docs)。

---

## Webhook 回调

无需轮询，通过 Webhook 接收结果：

```python
task_id = client.submit(
    task_type="cloudflare_turnstile",
    proxy="http://user:pass@ip:port",
    target_url="https://example.com",
    site_key="0x4AAAAAAA...",
    callback_url="https://your-server.com/webhook",
)
```

你的服务器会收到：

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

重试策略：如果未返回 HTTP 200，最多重试 3 次，间隔 5秒、30秒、120秒。

---

## 账户与计费

```python
# 查询余额
balance = client.get_balance()
print(f"${balance}")

# API Key 信息（状态、限额、今日消费）
info = client.get_key_info()
print(f"Key: {info['keyPrefix']}...")
print(f"状态: {'激活' if info['isActive'] else '未激活'}")
print(f"今日消费: ${info['todaySpent']}")
print(f"每日限额: {info['dailySpendLimit'] or '无限制'}")

# 消费统计（按天、按类型）
stats = client.get_spending_stats()
stats = client.get_spending_stats(queue="cloudflare_turnstile")

# 价格查询（无需认证）
for p in client.get_pricing():
    print(f"{p['name']}: ${p['price_per_solve']}/次, "
          f"~{p['avg_solve_time']}秒, 成功率{p['success_rate']}%")
```

---

## 配置

```python
client = PassXAPI(
    api_key="YOUR_API_KEY",
    polling_interval=1.5,  # 轮询间隔秒数（默认 1.5）
    timeout=120.0,         # 最大等待秒数（默认 120）
)
```

---

## 错误处理

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
    print("API Key 无效")
except ZeroBalanceError:
    print("余额不足，请充值：https://www.passxapi.com/app/billing/deposit")
except CaptchaUnsolvableError:
    print("验证码无法求解")
except BadParametersError as e:
    print(f"参数错误: {e}")
```

| 异常 | 错误码 | 触发条件 |
|------|--------|---------|
| `AuthError` | `ERROR_AUTH` | API Key 无效 |
| `ZeroBalanceError` | `ERROR_ZERO_BALANCE` | 余额不足 |
| `BadParametersError` | `ERROR_BAD_PARAMETERS` | 参数缺失或无效 |
| `CaptchaUnsolvableError` | `ERROR_CAPTCHA_UNSOLVABLE` | 求解失败/超时 |
| `TaskNotFoundError` | `ERROR_NO_SUCH_CAPCHA_ID` | 任务 ID 不存在 |
| `RateLimitError` | `ERROR_RATE_LIMIT` | 超出并发限制 |
| `DailyLimitError` | `ERROR_DAILY_LIMIT_REACHED` | 达到每日消费上限 |
| `IPNotAllowedError` | `ERROR_IP_NOT_ALLOWED` | IP 不在白名单内 |

> 失败请求**不收费**。

---

## 底层 API

```python
# 手动提交任务
task_id = client.submit(
    task_type="cloudflare_turnstile",
    proxy="http://user:pass@ip:port",
    target_url="https://example.com",
    site_key="0x4AAAAAAA...",
)

# 手动轮询结果
import time
while True:
    result = client.get_result(task_id)
    if result["status"] == "SUCCESS":
        print(result["result"]["token"])
        break
    time.sleep(1.5)
```

---

## 从 2Captcha 迁移

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

## 相关链接

| | |
|---|---|
| **官网** | https://www.passxapi.com |
| **注册** | https://www.passxapi.com/login |
| **API Keys** | https://www.passxapi.com/app/api-keys |
| **API 文档** | https://www.passxapi.com/docs |
| **控制台** | https://www.passxapi.com/app/dashboard |
| **价格** | https://www.passxapi.com/services |
| **客服** | contact@passxapi.com |

## 许可证

[MIT](LICENSE) © PassXAPI
