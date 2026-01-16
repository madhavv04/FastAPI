from fastapi import FastAPI
from pydantic import BaseModel

# ---------------------- REGISTER ----------------------
data =  [
    {
    "name" : "Alice",
    "email" : "alice@gmail.com",
    "password" : "Alice123"
    },
    
    {
    "name" : "John",
    "email" : "john@gmail.com",
    "password" : "john123"
    },
    
    {
    "name" : "Max",
    "email" : "max@gmail.com",
    "password" : "max123"
    },
    ]

# create a class for the register
class Register_user(BaseModel):
    name : str
    email : str
    password : str
    

app = FastAPI(title="User Login Page")

#Make a home url
@app.get("/")
def home_page():
    return {
        "message" : "API is running...!",
    }
    
#Display all users
@app.get("/users")
def all_users():
    return data

# Make the instance (object) of class = Register_user
@app.post("/register")
def register_user(user : Register_user):
    return user


# ---------------------- LOGIN ---------------------

class Login_user(BaseModel):
    email : str
    password : str

@app.post("/login")
def login_user(user : Login_user):
    for i in data:
        if i["email"] == user.email and i["password"] == user.password:
            return {
                "User" : i ,
                "message" : "User Login Successfully"
            }
    return {
        "message" : "User Not Found"
    }

# ---------------------- UPDATE ---------------------

class Update_user(BaseModel):
    email : str
    new_name : str
    new_email : str
    new_password : str
    
@app.put("/update")
def update_user(user : Update_user):
    for i in data:
        if i["email"] == user.email:
            i["name"] = user.new_name
            i["email"] = user.new_email
            i["password"] = user.new_password
            return {
            "message" : "User Updated Successfully",
            "User" : i
        }
    return {
        "message" : "User Not Found"
    }
    
# ---------------------- DELETE ---------------------

class Delete_user(BaseModel):
    email : str

@app.delete("/delete")
def delete_user(user : Delete_user):
    for i in data:
        if i["email"] == user.email:
            data.remove(i)
            return{
                "user" : i,
                "message" : "User Deleted Successfully"
            }

