from utils.db import users_collection
from models.user_model import user_schema
from utils.jwt_handler import generate_token

# CREATE USER
def create_user(data):
    required = ["name", "email", "role"]

    if not all(field in data for field in required):
        return {"error": "Missing fields"}, 400

    # Optional: check if user already exists
    existing_user = users_collection.find_one({"email": data["email"]})
    if existing_user:
        return {"error": "User already exists"}, 400

    users_collection.insert_one(data)
    return {"message": "User created"}, 201


# GET ALL USERS
def get_users():
    users = users_collection.find()
    return [user_schema(u) for u in users]


# LOGIN USER (JWT)
def login_user(data):
    email = data.get("email")

    if not email:
        return {"error": "Email required"}, 400

    user = users_collection.find_one({"email": email})

    if not user:
        return {"error": "User not found"}, 404

    # Generate JWT token
    token = generate_token(user)

    return {
        "message": "Login successful",
        "token": token
    }