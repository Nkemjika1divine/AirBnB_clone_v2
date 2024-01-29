#!/usr/bin/python3
""" This module is the homepage presened by Flask """
from flask import Flask
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """
    Function Docs
    """
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.{}'.format(state_id)
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def close_db(exception):
    """Close session"""
    storage.close()


if __name__ == "__main__":
    """Set the port and the ip"""
    app.run(port='5000', host='0.0.0.0')
