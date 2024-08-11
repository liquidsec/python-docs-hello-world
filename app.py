from flask import Flask
app = Flask(__name__)

@app.route("/subdomain-takeover-poc")
def hello():
    return "Subdomain Takeover PoC"
