import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Authentication App")

menu = st.sidebar.selectbox(
    "Choose Option",
    ["Signup", "Signin", "Google Login"]
)

if menu == "Signup":
    st.header("Signup")

    name = st.text_input("Enter Name")
    email = st.text_input("Enter Email")
    password = st.text_input("Enter Password", type="password")

    if st.button("Signup"):
        signup_data = {
            "name": name,
            "email": email,
            "password": password
        }

        response = requests.post(
            f"{API_URL}/signup",
            json=signup_data
        )

        data = response.json()

        if response.status_code == 200:
            st.success(data["message"])
        else:
            st.error(data["detail"])


if menu == "Signin":
    st.header("Signin")

    email = st.text_input("Enter Email")
    password = st.text_input("Enter Password", type="password")

    if st.button("Signin"):
        signin_data = {
            "email": email,
            "password": password
        }

        response = requests.post(
            f"{API_URL}/signin",
            json=signin_data
        )

        data = response.json()

        if response.status_code == 200:
            st.success(data["message"])
            st.write("JWT Token")
            st.code(data["token"])
        else:
            st.error(data["detail"])


if menu == "Google Login":
    st.header("Google Sign In")

    st.write("Click below button to login with Google")

    google_login_url = f"{API_URL}/google/login"

    st.link_button(
        "Sign in with Google",
        google_login_url
    )