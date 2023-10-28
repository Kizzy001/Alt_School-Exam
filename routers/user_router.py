from fastapi import APIRouter

from schema.user_schema import User

import csv

from csv import DictReader


import uuid

user_router = APIRouter()


with open("new.database") as file:

    dict_reader1 = DictReader (file)

    list_of_dict1 = list (dict_reader1)

    list_of_dict1



#create acct

def create_account ( user: User):
    with open ("new.database", "a", newline='') as file:
       
        writer = csv.writer(file)
        writer.writerow([user.id, user.firstname, user.lastname, user.username, user.email, user.password]) 

         

@user_router.post("/Create_new_account")
async def Account_creation ( user: User):

    for i in list_of_dict1:
        if i["username"] == user.username:
            return {"message": "Username already exist"}
        

    
    create_account(user)
    return {"message": "Account created successfully"}    


#login

@user_router.get("/Login")
async def login(username: str, password: str  ):
#     # with open ("new.database", "r") as file:
#     #     reader = csv.writer(file)

    for i in list_of_dict1:
        if i["username"] == username:
            if i["password"] == password:
                return {"message": "Login successfull", "data": f'You are welcome {i["username"]} '}

    return {"error": "Account does not exist, please register" }








    

