import os

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
MONGO_URI = os.getenv("MONGO_URI", "localhost")
MONGO_PORT = os.getenv("MONGO_PORT", 27017)
MONGO_DB_NAME = "simplon"

@app.route("/")
def hello_world():
    mongodb_client = MongoClient(MONGO_URI, MONGO_PORT)
    simplon_db = mongodb_client[MONGO_DB_NAME]

    html_text = "<ul>"
    for message in simplon_db.messages.find():
        html_text += "<li>{}</li>".format(message["text"])

    html_text += "</ul>"
    return html_text
