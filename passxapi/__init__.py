from passxapi.client import PassXAPI
from passxapi.exceptions import (
    PassXAPIError,
    AuthError,
    ZeroBalanceError,
    BadParametersError,
    CaptchaUnsolvableError,
    TaskNotFoundError,
    RateLimitError,
    DailyLimitError,
    IPNotAllowedError,
    AlreadyReportedError,
    TaskNotReadyError,
)

__version__ = "2.0.0"
__all__ = [
    "PassXAPI",
    "PassXAPIError",
    "AuthError",
    "ZeroBalanceError",
    "BadParametersError",
    "CaptchaUnsolvableError",
    "TaskNotFoundError",
    "RateLimitError",
    "DailyLimitError",
    "IPNotAllowedError",
    "AlreadyReportedError",
    "TaskNotReadyError",
]
