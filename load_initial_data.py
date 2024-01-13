import json
from pymongo import MongoClient
import glob
import time

# Vars - please change user and password according to your mongo_init.js
username = "envuser"
password = "envpass"

# Add a delay before attempting to connect to MongoDB
time.sleep(30)

# Connect to MongoDB Docker
connection_string = f"mongodb://{username}:{password}@localhost:27017/"
client = MongoClient(connection_string)
db = client['luftguete_db']
collection = db['linz_collection']

# Index all JSON files in the jsondump directory
json_files = glob.glob('jsondump/*.json')

# Push data into MongoDB
for file in json_files:
    with open(file) as f:
        data = json.load(f)
        insert_result = collection.insert_one(data)
        print(f"Inserted document with ID: {insert_result.inserted_id} from file: {file}")

# Check if data is in MongoDB
cursor = collection.find({})
for document in cursor:
    print(document)