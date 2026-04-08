from fastapi import FastAPI
from pathlib import Path
from pydantic import EmailStr
from schemas.user_schema import User,User_Update
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Welcome to demo application"}

DATA_FILE = Path(r"C:\Training\day-2\FastAPI-Task-2\backend\db\data.json")

def read_data():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.get("/get-users")
def get_items():
    return read_data()

@app.get("/create-user")
def create_item(User):
    users = read_data()
    users.append(User.dict())
    write_data(users)
    return users

@app.put("/update-user/{email}")
def update_item(email: EmailStr, User_Update):
    users = read_data()
    for i, user in enumerate(users):
        if users["email"] == email:
            users[i] = { "email": email, **User_Update.dict() }
            write_data(users)
            return users[i]
    return None


@app.delete("/delete-user/{email}")
def delete_item(email: EmailStr):
    users = read_data()
    new_users = [user for user in users if user["email"] != email]
    write_data(new_users)
    return {"message": "Deleted successfully"}