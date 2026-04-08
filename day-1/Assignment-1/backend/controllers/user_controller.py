import bcrypt
import jwt
import os

from dotenv import load_dotenv
from fastapi import HTTPException
from datetime import datetime, timedelta

from models.User_model import User
from schemas.user_schema import UserSignup, UserSignin

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")


async def signup_controller(user: UserSignup):
    existing_user = await User.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(
        user.password.encode("utf-8"),
        salt
    )

    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password.decode("utf-8")
    )

    await new_user.insert()

    return {
        "message": "User created successfully"
    }


async def signin_controller(user: UserSignin):
    existing_user = await User.find_one({"email": user.email})

    if not existing_user:
        raise HTTPException(
            status_code=400,
            detail="Invalid email or password"
        )

    password_match = bcrypt.checkpw(
        user.password.encode("utf-8"),
        existing_user.password.encode("utf-8")
    )

    if not password_match:
        raise HTTPException(
            status_code=400,
            detail="Invalid email or password"
        )

    token_data = {
        "user_id": str(existing_user.id),
        "email": existing_user.email,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }

    token = jwt.encode(
        token_data,
        SECRET_KEY,
        algorithm="HS256"
    )

    return {
        "message": "Login successful",
        "token": token
    }


async def google_login_controller(user_info):
    existing_user = await User.find_one({"email": user_info["email"]})

    if not existing_user:
        new_user = User(
            name=user_info["name"],
            email=user_info["email"],
            password=""
        )

        await new_user.insert()
        existing_user = new_user

    token_data = {
        "user_id": str(existing_user.id),
        "email": existing_user.email,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }

    token = jwt.encode(
        token_data,
        SECRET_KEY,
        algorithm="HS256"
    )

    return {
        "message": "Google login successful",
        "token": token,
        "user": {
            "name": existing_user.name,
            "email": existing_user.email
        }
    }