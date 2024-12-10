from pymongo.mongo_client import MongoClient
import json
import os

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)
db = client['wikidata_json']
occupation = "politician"
collection = db[occupation]
gt_user = "<YOUR GT USERNAME>" # ADD GT USERNAME HERE

parent_dir = "/home/hice1/"+gt_user+"/scratch/NL_Project/Data/English_Labelled_Wikidata_"+occupation

len_files = len([name for name in os.listdir(parent_dir) if os.path.isfile(name)])

for i in range(1, len_files+1):
    with open(parent_dir+"en_labelled_part"+ str(i)+".json") as f:
        data = json.load(f)
        print("Loaded JSON file for Part " + str(i))
        # Convert each entity to a format MongoDB can store
        documents = [{**{"_id": key}, **value} for key, value in data.items()]
        collection.insert_many(documents)
        print("Added data from Part " + str(i) + " to Database")


print("Creating Index based on Given name")
# Index 'given name' for fast search
collection.create_index("given name")
collection.create_index("Commons category")

# Test retrieval for the collection
results = collection.find({"given name": "John"})
for result in results:
    print(result)
    print("\n")