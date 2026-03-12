class PassXAPIError(Exception):
    """Base exception for PassXAPI errors."""

    def __init__(self, error_code: str, error_description: str = ""):
        self.error_code = error_code
        self.error_description = error_description
        super().__init__(f"{error_code}: {error_description}" if error_description else error_code)


class AuthError(PassXAPIError):
    pass


class ZeroBalanceError(PassXAPIError):
    pass


class BadParametersError(PassXAPIError):
    pass


class CaptchaUnsolvableError(PassXAPIError):
    pass


class TaskNotFoundError(PassXAPIError):
    pass


class RateLimitError(PassXAPIError):
    pass


class DailyLimitError(PassXAPIError):
    pass


class IPNotAllowedError(PassXAPIError):
    pass


class AlreadyReportedError(PassXAPIError):
    pass


class TaskNotReadyError(PassXAPIError):
    pass


ERROR_MAP = {
    "ERROR_AUTH": AuthError,
    "ERROR_ZERO_BALANCE": ZeroBalanceError,
    "ERROR_BAD_PARAMETERS": BadParametersError,
    "ERROR_CAPTCHA_UNSOLVABLE": CaptchaUnsolvableError,
    "ERROR_NO_SUCH_CAPCHA_ID": TaskNotFoundError,
    "ERROR_RATE_LIMIT": RateLimitError,
    "ERROR_DAILY_LIMIT_REACHED": DailyLimitError,
    "ERROR_IP_NOT_ALLOWED": IPNotAllowedError,
    "ERROR_ALREADY_REPORTED": AlreadyReportedError,
    "ERROR_TASK_NOT_READY": TaskNotReadyError,
}


def raise_for_error(data: dict):
    """Raise typed exception if response contains an error."""
    if data.get("errorId", 0) != 0:
        code = data.get("errorCode", "UNKNOWN_ERROR")
        desc = data.get("errorDescription", "")
        exc_cls = ERROR_MAP.get(code, PassXAPIError)
        raise exc_cls(code, desc)
