

import pymongo

myclient = pymongo.MongoClient('mongodb+srv://nandesh:Nandesh31@cluster0.oxqazmd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
mydb = myclient['mydatabase']
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print(x)
