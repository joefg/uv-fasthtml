from fasthtml import Beforeware
from time import time
from starlette.responses import JSONResponse

# Simple in-memory fixed-window limiter (per IP)
WINDOW_SECONDS = 60
MAX_REQUESTS = 100
requests_store = {}  # {ip: {"window_start": float, "count": int}}

def rate_limit_before(req, sess):
    client_ip = req.client.host  # depending on FastHTML/Starlette request object
    now = time()

    data = requests_store.get(client_ip, {"window_start": now, "count": 0})

    if now - data["window_start"] >= WINDOW_SECONDS:
        data = {"window_start": now, "count": 0}

    if data["count"] >= MAX_REQUESTS:
        return JSONResponse(
            {"detail": "Rate limit exceeded"},
            status_code=429,
            headers={
                "X-RateLimit-Limit": str(MAX_REQUESTS),
                "X-RateLimit-Remaining": "0",
                "X-RateLimit-Reset": str(int(data["window_start"] + WINDOW_SECONDS)),
            },
        )

    data["count"] += 1
    requests_store[client_ip] = data

    sess["rate_limit"] = {
        "limit": MAX_REQUESTS,
        "remaining": MAX_REQUESTS - data["count"],
        "reset": int(data["window_start"] + WINDOW_SECONDS),
    }

rate_limiter = Beforeware(rate_limit_before, skip=["/health"])
