import pymongo

from config import USER, PASSWORD

url = f'mongodb+srv://{USER}:{PASSWORD}' \
      '@cluster0.dz6svwl.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(url)

db = client.booksDB
fantasy_collection = db.fantasy
school_collection = db.school

# create collections
fantasy_collection.insert_one(
      {'name': "Гра престолів", "price": 120, "year": 1996, "pages": 835}
)

school_collection.insert_many([
      {'name': "Алгебра", "grade": 8, "year": 2021, "pages": 75},
      {'name': "Історія", "grade": 10, "year": 2020, "pages": 120},
      {'name': "Англійська мова", "grade": 5, "year": 2017, "pages": 90},
      {'name': "Українська мова", "grade": 11, "year": 1996, "pages": 103},
      {'name': "Географія", "grade": 9, "year": 2023, "pages": 83}
])


# Find history book
history_book = school_collection.find_one({"name": "Історія"})
print(history_book)

# Update game of thrones price
query = {"name": "Гра престолів"}
operation = {"$inc": {"price": 56}}
data = fantasy_collection.update_one(query, operation)
print(data.raw_result)


# Delete game of thrones
data2 = fantasy_collection.delete_many(query)
print(data2.raw_result)

# delete books with year lower than 2020
query2 = {"year": {"$lt": 2020}}
data3 = school_collection.delete_many(query2)
print(data3.raw_result)
