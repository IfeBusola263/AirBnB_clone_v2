#!/usr/bin/python3
"""
This module starts a flask web -application
"""

from flask import Flask, render_template
from os import getenv
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id=None):
    """This function returns the list of states in the database"""

    # Either for DB or file storage
    if id is None:
        states = storage.all(State)
        return render_template('9-states.html', states=states)

    # When We have an ID
    else:
        states_cities = {}
        states = storage.all(State)
        for state in states.values():
            cities = []
            # Handled by DB
            if state.id == id and getenv('HBNB_TYPE_STORAGE') == 'db':
                for city in state.cities:
                    cities.append(city)
                states_cities[state] = cities
                return render_template('9-states.html', states=states_cities)

            elif state.id == id:
                # Handled by filestorage
                for city in state.cities():
                    cities.append(city)
                states_cities[state] = cities
                return render_template('9-states.html', states=states_cities)

        return render_template('9-states.html', states='Not found!')


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    """ This closes the session
    """
    storage.close()


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
