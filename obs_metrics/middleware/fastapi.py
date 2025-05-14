import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from ..logger import Logger

logger = Logger()

class FastApiMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time

        log_data = {
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "duration_ms": round(duration * 1000, 2),
            "client_ip": request.client.host if request.client else None,
            "user_agent": request.headers.get("user-agent"),
            "trace_id": request.headers.get("x-trace-id")
        }

        level = "info" if response.status_code < 400 else "error"
        logger.__getattribute__(level)("HTTP request", context=log_data)

        return response