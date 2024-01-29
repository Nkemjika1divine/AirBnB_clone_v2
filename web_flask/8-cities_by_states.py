#!/usr/bin/python3
"""Documentation"""
from flask import Flask
from models import *
from models import storage


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Documentation"""
    storage.close()


if __name__ == "__main__":
    """Set the port and the ip"""
    app.run(port='5000', host='0.0.0.0')
