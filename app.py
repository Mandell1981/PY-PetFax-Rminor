# config                    
from flask import Flask
app = Flask(__name__)


#index route
@app.route('/')
def index():
    return 'Hello, this is PetFax!'



@app.route('/pets')
def pets():
    return 'This is a list of pets available for adoption'
