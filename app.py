import datetime
from logging import Formatter
from flask import Flask, render_template, request
from pymongo import MongoClient #to open up client side session

import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.pepBlog

    entries=[]

    @app.route("/", methods=["GET", "POST"])
    def home():
        # print([e for e in app.db.entries.find({})])

        if request.method ==  "POST":
            newPostContent = request.form.get("content")
            formattedDate = datetime.datetime.today().strftime("%Y-%m-%d")
            # entries.append((newPostContent, formattedDate))
            app.db.entries.insert_one({"content":newPostContent, "date":formattedDate})

        entries_with_date = [
            (entry["content"],
            entry["date"],
            datetime.datetime.strptime(entry["date"],"%Y-%m-%d").strftime("%b %d")
            )

            for entry in app.db.entries.find({})
            #return data from mongoDB as a list of dictionaries, then we make tuples in the desired format
        ]
        
        return render_template("home.html", entries=entries_with_date)
    
    return app;
