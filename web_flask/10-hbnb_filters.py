#!/usr/bin/python3
""" This module is the homepage presened by Flask """
from flask import Flask
from models import *
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """
    Function Docs
    """
    amen = storage.all("Amenity").values()
    states = storage.all("State").values()
    return render_template('10-hbnb_filters.html', states=states, amen=amen)


@app.teardown_appcontext
def teardown_db(exception):
    """Close session"""
    storage.close()


if __name__ == "__main__":
    """Set the port and the ip"""
    app.run(port='5000', host='0.0.0.0')
