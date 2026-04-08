from fastapi import APIRouter, Request
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from dotenv import load_dotenv
import os

from controllers.user_controller import (
    signup_controller,
    signin_controller,
    google_login_controller
)
from schemas.user_schema import UserSignup, UserSignin

load_dotenv()

router = APIRouter()

config_data = {
    "GOOGLE_CLIENT_ID": os.getenv("GOOGLE_CLIENT_ID"),
    "GOOGLE_CLIENT_SECRET": os.getenv("GOOGLE_CLIENT_SECRET")
}

config = Config(environ=config_data)

oauth = OAuth(config)

oauth.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid email profile"
    }
)


@router.post("/signup")
async def signup(user: UserSignup):
    return await signup_controller(user)


@router.post("/signin")
async def signin(user: UserSignin):
    return await signin_controller(user)


@router.get("/google/login")
async def google_login(request: Request):
    redirect_uri = request.url_for("google_auth")

    return await oauth.google.authorize_redirect(
        request,
        redirect_uri
    )


@router.get("/google/auth", name="google_auth")
async def google_auth(request: Request):
    token = await oauth.google.authorize_access_token(request)

    user_info = token.get("userinfo")

    return await google_login_controller(user_info)