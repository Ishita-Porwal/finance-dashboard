from flask import request
from functools import wraps
from utils.jwt_handler import decode_token

def role_required(allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization")

            if not token:
                return {"error": "Token missing"}, 401

            decoded = decode_token(token)

            if not decoded:
                return {"error": "Invalid token"}, 401

            role = decoded.get("role")

            if role not in allowed_roles:
                return {"error": "Unauthorized"}, 403

            return func(*args, **kwargs)

        return wrapper
    return decorator