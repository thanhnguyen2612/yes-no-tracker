#! /usr/bin/python3
import os, requests

from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

# Set up database
engine = create_engine("postgres://kfhiibmrwdbzvr:66d092d68c643255f9ff53093acef12e044b50b8c116dc2134ed8113ae341712@ec2-46-137-84-140.eu-west-1.compute.amazonaws.com:5432/d1lj599f4t202j")
db = scoped_session(sessionmaker(bind=engine))

# Index page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/thank", methods=["POST"])
def thank():
    selection = request.form.get("selection")
    db.execute("INSERT INTO user_selection (selection) VALUES (:selection)", {"selection": selection})
    db.commit()
