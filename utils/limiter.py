from slowapi.util import get_ipaddr
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler

limiter = Limiter(key_func = get_ipaddr)

