import time
from typing import Optional, Dict, Any

import requests

from passxapi.exceptions import raise_for_error, CaptchaUnsolvableError, PassXAPIError


BASE_URL = "https://api.passxapi.com/api/v1"


class PassXAPI:
    """PassXAPI Python SDK client.

    Usage::

        from passxapi import PassXAPI

        client = PassXAPI("your_api_key")
        result = client.cloudflare_turnstile(
            target_url="https://example.com",
            site_key="0x4AAAAAAA...",
            proxy="http://user:pass@ip:port",
        )
        print(result["token"])
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = BASE_URL,
        polling_interval: float = 1.5,
        timeout: float = 120.0,
    ):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.polling_interval = polling_interval
        self.timeout = timeout
        self._session = requests.Session()
        self._session.headers.update({
            "x-api-key": api_key,
            "Content-Type": "application/json",
        })

    # ── Core API ────────────────────────────────────────────────────

    def submit(self, task_type: str, proxy: str, target_url: str,
               callback_url: Optional[str] = None, **params) -> str:
        """Submit a task. Returns task_id."""
        data = {
            "task_type": task_type,
            "proxy": proxy,
            "target_url": target_url,
            **params,
        }
        if callback_url:
            data["callback_url"] = callback_url
        resp = self._post("/task/submit", data)
        if not resp.get("ok"):
            raise PassXAPIError(
                resp.get("errorCode", "SUBMIT_FAILED"),
                resp.get("errorDescription", str(resp)),
            )
        return resp["task_id"]

    def get_result(self, task_id: str) -> dict:
        """Get task result. Returns raw response dict."""
        resp = self._get(f"/task/result/{task_id}")
        return resp

    def solve(self, task_type: str, proxy: str, target_url: str,
              callback_url: Optional[str] = None, **params) -> dict:
        """Submit + poll until done. Returns the result dict.

        Result contains keys like: token, cookies, ua, request_token
        depending on the captcha type.
        """
        task_id = self.submit(task_type, proxy, target_url,
                              callback_url=callback_url, **params)
        deadline = time.monotonic() + self.timeout

        while time.monotonic() < deadline:
            result = self.get_result(task_id)
            status = result.get("status", "").upper()

            if status == "SUCCESS":
                return result.get("result", result)
            elif status == "FAILED":
                raise CaptchaUnsolvableError(
                    result.get("errorCode", "ERROR_CAPTCHA_UNSOLVABLE"),
                    result.get("errorDescription", f"Task {task_id} failed"),
                )
            # Still processing
            time.sleep(self.polling_interval)

        raise CaptchaUnsolvableError(
            "ERROR_CAPTCHA_UNSOLVABLE",
            f"Task {task_id} timed out after {self.timeout}s",
        )

    # ── reCAPTCHA v3 ────────────────────────────────────────────────

    def recaptcha_v3(
        self,
        target_url: str,
        proxy: str,
        site_key: str,
        action: str = "verify",
        enterprise: bool = False,
        title: Optional[str] = None,
        **kw,
    ) -> dict:
        """Solve reCAPTCHA v3."""
        params = {"site_key": site_key, "action": action, "enterprise": enterprise}
        if title:
            params["title"] = title
        return self.solve("recaptcha_v3", proxy, target_url, **params, **kw)

    # ── hCaptcha ────────────────────────────────────────────────────

    def hcaptcha(
        self,
        target_url: str,
        proxy: str,
        site_key: str,
        **kw,
    ) -> dict:
        """Solve hCaptcha."""
        return self.solve("hcaptcha", proxy, target_url, site_key=site_key, **kw)

    def hcaptcha_pro(
        self,
        target_url: str,
        proxy: str,
        **kw,
    ) -> dict:
        """Solve hCaptcha Pro (Enterprise)."""
        return self.solve("hcaptcha_pro", proxy, target_url, **kw)

    # ── Cloudflare ──────────────────────────────────────────────────

    def cloudflare_turnstile(
        self,
        target_url: str,
        proxy: str,
        site_key: str,
        **kw,
    ) -> dict:
        """Solve Cloudflare Turnstile."""
        return self.solve("cloudflare_turnstile", proxy, target_url,
                          site_key=site_key, **kw)

    def cloudflare_waf(
        self,
        target_url: str,
        proxy: str,
        target_method: str = "GET",
        **kw,
    ) -> dict:
        """Solve Cloudflare WAF (5-second shield / JS Challenge)."""
        return self.solve("cloudflare_waf", proxy, target_url,
                          target_method=target_method, **kw)

    # ── Akamai ──────────────────────────────────────────────────────

    def akamai(
        self,
        target_url: str,
        proxy: str,
        akamai_js_url: str,
        page_fp: Optional[str] = None,
        **kw,
    ) -> dict:
        """Solve Akamai Bot Manager."""
        params: Dict[str, Any] = {"akamai_js_url": akamai_js_url}
        if page_fp:
            params["page_fp"] = page_fp
        return self.solve("akamai", proxy, target_url, **params, **kw)

    def akamai_sec_cpt(
        self,
        target_url: str,
        proxy: str,
        sec_cpt: str,
        sec_json: dict,
        **kw,
    ) -> dict:
        """Solve Akamai sec_cpt secondary challenge."""
        return self.solve("akamai_sec_cpt", proxy, target_url,
                          sec_cpt=sec_cpt, sec_json=sec_json, **kw)

    # ── PerimeterX ──────────────────────────────────────────────────

    def perimeterx_silent(
        self,
        target_url: str,
        proxy: str,
        perimeterx_js_url: str,
        pxAppId: str,
        **kw,
    ) -> dict:
        """Solve PerimeterX silent detection."""
        return self.solve("perimeterx_silent", proxy, target_url,
                          perimeterx_js_url=perimeterx_js_url,
                          pxAppId=pxAppId, **kw)

    def perimeterx_challenge(
        self,
        target_url: str,
        proxy: str,
        pxvid: str,
        pxuuid: str,
        pxAppId: str,
        perimeterx_js_url: str,
        captcha_js_url: str,
        init_cookies: dict,
        **kw,
    ) -> dict:
        """Solve PerimeterX interactive challenge."""
        return self.solve("perimeterx_challenge", proxy, target_url,
                          pxvid=pxvid, pxuuid=pxuuid, pxAppId=pxAppId,
                          perimeterx_js_url=perimeterx_js_url,
                          captcha_js_url=captcha_js_url,
                          init_cookies=init_cookies, **kw)

    # ── Kasada ──────────────────────────────────────────────────────

    def kasada_ct(
        self,
        target_url: str,
        proxy: str,
        protected_api_domain: str,
        kasada_js_domain: str,
        **kw,
    ) -> dict:
        """Solve Kasada ct."""
        return self.solve("kasada_ct", proxy, target_url,
                          protected_api_domain=protected_api_domain,
                          kasada_js_domain=kasada_js_domain, **kw)

    def kasada_cd(
        self,
        target_url: str,
        proxy: str,
        ct: str,
        st: str,
        fc: str,
        site: str,
        **kw,
    ) -> dict:
        """Solve Kasada cd (advanced protection)."""
        return self.solve("kasada_cd", proxy, target_url,
                          ct=ct, st=st, fc=fc, site=site, **kw)

    def kasada_tl_payload(
        self,
        target_url: str,
        proxy: str,
        **kw,
    ) -> dict:
        """Generate Kasada TL Payload."""
        return self.solve("kasada_tl_payload", proxy, target_url, **kw)

    # ── DataDome ────────────────────────────────────────────────────

    def datadome_silent(
        self,
        target_url: str,
        proxy: str,
        target_method: str = "GET",
        **kw,
    ) -> dict:
        """Solve DataDome silent detection."""
        return self.solve("datadome_silent", proxy, target_url,
                          target_method=target_method, **kw)

    def datadome_invisible(
        self,
        target_url: str,
        proxy: str,
        datadome_js_url: str,
        ddjskey: str,
        ddoptions: str,
        **kw,
    ) -> dict:
        """Solve DataDome invisible captcha."""
        return self.solve("datadome_invisible", proxy, target_url,
                          datadome_js_url=datadome_js_url,
                          ddjskey=ddjskey, ddoptions=ddoptions, **kw)

    def datadome_slider(
        self,
        target_url: str,
        proxy: str,
        target_method: str = "GET",
        init_cookies: Optional[dict] = None,
        **kw,
    ) -> dict:
        """Solve DataDome slider captcha."""
        params: Dict[str, Any] = {"target_method": target_method}
        if init_cookies:
            params["init_cookies"] = init_cookies
        return self.solve("datadome_slider", proxy, target_url, **params, **kw)

    # ── Shape Security ──────────────────────────────────────────────

    def shape(
        self,
        target_url: str,
        proxy: str,
        target_api: str,
        shape_js_url: str,
        method: str = "GET",
        title: Optional[str] = None,
        **kw,
    ) -> dict:
        """Solve Shape Security (F5)."""
        params: Dict[str, Any] = {
            "target_api": target_api,
            "shape_js_url": shape_js_url,
            "method": method,
        }
        if title:
            params["title"] = title
        return self.solve("shape", proxy, target_url, **params, **kw)

    # ── FunCaptcha ──────────────────────────────────────────────────

    def funcaptcha(
        self,
        target_url: str,
        proxy: str,
        public_key: str,
        custom_api_host: Optional[str] = None,
        **kw,
    ) -> dict:
        """Solve FunCaptcha (Arkose Labs)."""
        params: Dict[str, Any] = {"public_key": public_key}
        if custom_api_host:
            params["custom_api_host"] = custom_api_host
        return self.solve("funcaptcha", proxy, target_url, **params, **kw)

    # ── Vercel Challenge ────────────────────────────────────────────

    def vercel_challenge(
        self,
        target_url: str,
        proxy: str,
        **kw,
    ) -> dict:
        """Solve Vercel Challenge."""
        return self.solve("vercel_challenge", proxy, target_url, **kw)

    # ── Castle ──────────────────────────────────────────────────────

    def castle(
        self,
        target_url: str,
        proxy: str,
        config_json: dict,
        **kw,
    ) -> dict:
        """Solve Castle anti-fraud. config_json: {"pk": "...", "avoidCookies": bool}"""
        return self.solve("castle", proxy, target_url,
                          config_json=config_json, **kw)

    # ── Reese84 ─────────────────────────────────────────────────────

    def reese84(
        self,
        target_url: str,
        proxy: str,
        reese84_js_url: str,
        **kw,
    ) -> dict:
        """Solve Reese84 (Imperva)."""
        return self.solve("reese84", proxy, target_url,
                          reese84_js_url=reese84_js_url, **kw)

    # ── UTMVC ───────────────────────────────────────────────────────

    def utmvc(
        self,
        target_url: str,
        proxy: str,
        utmvc_js_url: str,
        incap_cookie: dict,
        **kw,
    ) -> dict:
        """Solve UTMVC (Imperva legacy)."""
        return self.solve("utmvc", proxy, target_url,
                          utmvc_js_url=utmvc_js_url,
                          incap_cookie=incap_cookie, **kw)

    # ── Sbsd ────────────────────────────────────────────────────────

    def sbsd(
        self,
        target_url: str,
        proxy: str,
        sbsd_js_url: str,
        init_cookies: dict,
        **kw,
    ) -> dict:
        """Solve Sbsd (Ticketmaster etc.)."""
        return self.solve("sbsd", proxy, target_url,
                          sbsd_js_url=sbsd_js_url,
                          init_cookies=init_cookies, **kw)

    # ── AWS WAF ─────────────────────────────────────────────────────

    def aws(
        self,
        target_url: str,
        proxy: str,
        aws_js_url: str,
        **kw,
    ) -> dict:
        """Solve AWS WAF Captcha."""
        return self.solve("aws", proxy, target_url,
                          aws_js_url=aws_js_url, **kw)

    # ── CaptchaFox ──────────────────────────────────────────────────

    def captchafox(
        self,
        target_url: str,
        proxy: str,
        site_key: str,
        **kw,
    ) -> dict:
        """Solve CaptchaFox (GDPR-compliant)."""
        return self.solve("captchafox", proxy, target_url,
                          site_key=site_key, **kw)

    # ── Forter ──────────────────────────────────────────────────────

    def forter(
        self,
        target_url: str,
        proxy: str,
        forter_js_url: str,
        site_id: str,
        **kw,
    ) -> dict:
        """Solve Forter anti-fraud."""
        return self.solve("forter", proxy, target_url,
                          forter_js_url=forter_js_url,
                          site_id=site_id, **kw)

    # ── ThreatMetrix ────────────────────────────────────────────────

    def threatmetrix(
        self,
        target_url: str,
        proxy: str,
        org_id: str,
        page_id: str,
        session_id: str,
        custom_domain: str,
        title: Optional[str] = None,
        **kw,
    ) -> dict:
        """Solve ThreatMetrix (LexisNexis)."""
        params: Dict[str, Any] = {
            "org_id": org_id,
            "page_id": page_id,
            "session_id": session_id,
            "custom_domain": custom_domain,
        }
        if title:
            params["title"] = title
        return self.solve("threatmetrix", proxy, target_url, **params, **kw)

    # ── TLS Forward ─────────────────────────────────────────────────

    def tls_forward(
        self,
        target_url: str,
        proxy: str,
        **kw,
    ) -> dict:
        """TLS fingerprint forwarding proxy. Bypasses JA3/JA4 detection."""
        return self.solve("tls_forward", proxy, target_url, **kw)

    # ── Account & Billing ──────────────────────────────────────────

    def get_balance(self) -> float:
        """Get account balance in USD."""
        resp = self._post("/captcha/getBalance", {})
        if resp.get("errorId", 0) != 0:
            raise_for_error(resp)
        return resp["balance"]

    def get_spending_stats(
        self,
        date: Optional[int] = None,
        queue: Optional[str] = None,
    ) -> list:
        """Get spending statistics.

        Args:
            date: Unix timestamp for which day to query (default: today).
            queue: Filter by captcha type (e.g. "cloudflare_turnstile").

        Returns list of dicts with: dateFrom, dateTill, volume, money.
        """
        params: Dict[str, Any] = {}
        if date is not None:
            params["date"] = date
        if queue:
            params["queue"] = queue
        resp = self._post("/captcha/getSpendingStats", params)
        if resp.get("errorId", 0) != 0:
            raise_for_error(resp)
        return resp.get("data", [])

    def get_pricing(self) -> list:
        """Get pricing for all captcha types (no auth required).

        Returns list of dicts with: captcha_type, name, price_per_1k,
        price_per_solve, avg_solve_time, success_rate.
        """
        r = requests.post(f"{self.base_url}/captcha/getPricing", json={})
        r.raise_for_status()
        resp = r.json()
        return resp.get("pricing", [])

    def get_key_info(self) -> dict:
        """Get current API key info.

        Returns dict with: keyName, keyPrefix, isActive, createdAt,
        expiresAt, lastUsedAt, dailySpendLimit, todaySpent,
        ipWhitelist, balance.
        """
        resp = self._post("/captcha/getKeyInfo", {})
        if resp.get("errorId", 0) != 0:
            raise_for_error(resp)
        return resp

    # ── Internal ────────────────────────────────────────────────────

    def _post(self, path: str, data: dict) -> dict:
        r = self._session.post(f"{self.base_url}{path}", json=data)
        r.raise_for_status()
        return r.json()

    def _get(self, path: str) -> dict:
        r = self._session.get(f"{self.base_url}{path}")
        r.raise_for_status()
        return r.json()
