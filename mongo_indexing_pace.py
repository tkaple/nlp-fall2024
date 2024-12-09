from pymongo.mongo_client import MongoClient
import json

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)
db = client['wikidata_json']
collection = db['businessperson']
gt_user = "adeshpande322"

parent_dir = "/home/hice1/"+gt_user+"/scratch/NL_Project/Data/English_Labelled_Wikidata_businessperson/"

for i in range(1, 5):
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

results = collection.find({"given name": "John"})
for result in results:
    print(result)
    print("\n")