import datetime

import pymongo
import json
import os
from tqdm import tqdm

credentials = json.load(open("credentials.json"))

client = pymongo.MongoClient(
    username=credentials["mongodb"]["username"],
    password=credentials["mongodb"]["password"],
)

data = json.load(open(os.path.join("data", "chat_messages.json")))

for row in tqdm(data):
    if "time" in row:
        row["time"] = datetime.datetime.fromtimestamp(row["time"])

client.message_db.raw_messages.insert_many(data)
