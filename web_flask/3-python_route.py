#!/usr/bin/python3
""" This module is the homepage presened by Flask """
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def homepage_task0():
    """This returns the homepage"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def page_hbnb_task1():
    """This returns a HBNB page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def page_c_text_task2(text):
    """This returns a page showing a text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def page_python_text_task3(text="is cool"):
    """This returns a page showing a text"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    """Set the port and the ip"""
    app.run(port='5000', host='0.0.0.0')
