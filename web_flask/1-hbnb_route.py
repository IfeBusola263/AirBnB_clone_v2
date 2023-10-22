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


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
