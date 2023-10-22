#!/usr/bin/python3
'''
This is module starts a flask web application
'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''
    The serves the content in this route
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def home():
    '''
    The serves the content in /hbnb folder
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    '''
    The serves the content with a variable
    '''
    if '_' in text:
        new_text = text.replace('_', ' ')
        return f'C {new_text}'
    else:
        return f'C {text}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_py(text='is cool'):
    '''
    The serves the content with a variable
    '''
    if '_' in text:
        new_text = text.replace('_', ' ')
        return f'Python {new_text}'
    else:
        return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def display_int(n):
    '''
    The function displays the variable if it's an integer
    '''
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
