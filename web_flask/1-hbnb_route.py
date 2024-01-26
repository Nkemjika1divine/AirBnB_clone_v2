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


if __name__ == "__main__":
    """Set the port and the ip"""
    app.run(port='5000', host='0.0.0.0')
