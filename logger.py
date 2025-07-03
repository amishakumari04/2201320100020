from starlette.middleware.base import BaseHTTPMiddleware
import datetime

class CustomLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = datetime.datetime.utcnow()
        response = await call_next(request)
        log_entry = f"{start_time} - {request.method} {request.url.path} - {response.status_code}\n"
        with open("logs.txt", "a") as log_file:
            log_file.write(log_entry)
        return response
