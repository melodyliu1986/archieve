__author__ = 'liusong'

"""
This is a simple code to start learning Flask.
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

# Static path.
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/index/")
def index():
    return "Index Page"

# Dynamic path.
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)

# The main page.
@app.route("/main")
def csv():
    return render_template("csv.html")

# Error handler.
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run()
