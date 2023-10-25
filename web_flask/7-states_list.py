#!/usr/bin/python3
"""This module starts a flask web -application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """This function returns the list of states in the database"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    """ This closes the session
    """
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
