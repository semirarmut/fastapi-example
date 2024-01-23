import time

from fastapi import Request

from app.utils.app_logger import app_logger


async def log_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    log_dict = {
        'url': request.url.path,
        'method': request.method,
        'process_time': process_time,
        'res_code': response.status_code
    }
    app_logger.info(log_dict, extra=log_dict)
    response.headers["X-Process-Time"] = str(process_time)

    return response
