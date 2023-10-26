#!/usr/bin/python3
"""
This module starts a flask web -application
"""

from flask import Flask, render_template
from os import getenv
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def state_cities_list():
    """This function returns the list of states in the database"""

    states_cities = {}
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        states = storage.all(State)

        # get cities from the state object
        for state in states.values():
            cities = []
            for city in state.cities:
                cities.append(city)
            states_cities[state] = cities
    else:
        # from file storage
        states = storage.all(State)

        for state in states.values():
            cities = []
            for city in state.cities():
                cities.append(city)
            states_cities[state] = cities
    return render_template('8-cities_by_states.html',
                           states_cities=states_cities)



@app.teardown_appcontext
def teardown_appcontext(exception=None):
    """ This closes the session
    """
    storage.close()


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
