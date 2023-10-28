import csv

#Create a new csv file

header = ["id", "firstname", "lastname", "username", "email", "password"]

with open ("new.database", "w") as file:
    writer = csv.writer(file)
    writer.writerow(header)


#Create another csv file for blog

header = ["Author", "Title", "Body"]

with open("new.article_database", "w") as file:
    writer = csv.writer(file)
    writer.writerow(header)
