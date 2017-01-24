from flask import Flask, render_template, request, jsonify, url_for
from google.cloud import datastore

app = Flask(__name__)
ds_client = datastore.Client()

kind = 'Product'

print("hello world - johns first app")


@app.route("/")
def index():
    return "we fucking did it!"

@app.route("/autocomp")
def autocomp():
    return  "some fuckiong json here"



app.run(debug=True)

