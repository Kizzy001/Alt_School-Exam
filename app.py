from fastapi import FastAPI
from pydantic import BaseModel
from routers.user_router import user_router
from routers.blog_router import blog_router
# from blog.blog_main import create_article


import csv

app = FastAPI()

# class User (BaseModel):
#     id: int
#     firstname: str
#     lastname: str
#     username: str
#     email: str

app.include_router(user_router, prefix= "/Home", tags=['Users'])
app.include_router(blog_router, prefix ="/Blogs", tags=['Blogs'])


#Get home page

@app.get("/")
async def home():
    return {"Welcome To The Home Page"}


#Get about page

@app.get("/About_page")
async def About():
    return {"Welcome To The About Page"}

#Get Contact page

@app.get("/Contact_page")
async def Contact():
    return {"Welcome To The Contact Page"}

# #create acct

# data = []

# with open("new.database") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         data.append(row)

# # print (data)

# @app.post("/User")
# async def create_account (user: User):
#     with open ("new.database", "a", newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([user.id, user.firstname, user.lastname, user.username, user.email]) 


#         i = user.id
#         if i in data:
#             return {"Error": "User already exist"} 

#     return {"message": "Account created successfully", "data": user}

# #login

# @app.get("/User/Login")
# async def login(username: str, email: str, user: User ):
#     with open ("new.database", "r") as file:
#         reader = csv.writer(file)

      
       

#     return {"message": "Login successfull", "data": user}



