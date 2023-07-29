# save this as app.py
from flask import Flask

app = Flask('Flask')

@app.route("/")
def hello():
    return "Hello!"