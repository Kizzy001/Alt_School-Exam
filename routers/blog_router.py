from fastapi import APIRouter

import csv

from schema.blog_schema import Blog

from csv import DictReader

blog_router = APIRouter()

# @blog_router.post("/")
# async def create_account (blog: Blog):
#     with open ("new.database", "a", newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([blog.author, blog.title ]) 


#         # i = user.id
#         # if i in data:
#         #     return {"Error": "User already exist"} 

#     return {"message": "Account created successfully", "data": blog}



# all_article = {}
   

# with open("new.article_database") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         all_article.append(row)


# filename = "new.article_database"

# with open(filename, "r") as file:
#     for line in csv.DictReader(file):        
#       print (  line)

with open("new.article_database") as file:

    dict_reader = DictReader (file)

    list_of_dict = list (dict_reader)

    list_of_dict







#For blog
@blog_router.post("/Create_article")
async def create_article (blog: Blog):

    with open ("new.article_database", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([blog.author, blog.title, blog.body])
    return {"message": "Article cretaed successfully", "data": blog}

# @app.post("/User")
# async def create_account (user: User):
#     with open ("new.database", "a", newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([user.id, user.firstname, user.lastname, user.username, user.email]) 


#         i = user.id
#         if i in data:
#             return {"Error": "User already exist"} 

#     return {"message": "Account created successfully", "data": user}


#To edit the article
@blog_router.post("/Edit_article")
def edit_article ():
    return {"message": "Article Edited successfully"}

#Get all blog posts

@blog_router.get("/")
def Get_all_articles():
    return list_of_dict

#get article by title

@blog_router.get("/{title}")
async def get_article_by_title(title: str):
    for article_title in list_of_dict:
        if article_title["Title"] == title:
            return article_title
        
    
    return {"Error": "Title not found"}

