from flask import Blueprint, request
from services.user_service import create_user, get_users, login_user
from middleware.auth_middleware import role_required

user_bp = Blueprint("users", __name__)

# 🔐 LOGIN (NO AUTH REQUIRED)
@user_bp.route("/login", methods=["POST"])
def login():
    return login_user(request.json)


# 👤 CREATE USER (ADMIN ONLY)
@user_bp.route("/users", methods=["POST"])
@role_required(["Admin"])
def add_user():
    return create_user(request.json)


# 📄 GET USERS (ADMIN ONLY)
@user_bp.route("/users", methods=["GET"])
@role_required(["Admin"])
def fetch_users():
    return get_users()