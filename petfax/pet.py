from flask import (Blueprint, render_template)
import json

pets = json.load(open('pets.json'))


bp = Blueprint('pet', __name__, url_prefix="/pets")

#index route
@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)

#show route
@bp.route('/pets/<int:id>')
def show(id):
    pet = pets[id - 1]
    return render_template('pets/show.html', pet=pet)

'''
@bp.route('/create')
def create():
   # return render_template('create.html', pets=pets)
    return render_template('create.html')

@bp.route('/facts/new', methods=['GET'])
def new_fact():
    return render_template('new_fact.html')

@bp.route('/facts', methods=['POST'])
def submit_fact():
    submitter = request.form['submitter']
    fact = request.form['fact']
    return f"Submitter: {submitter}, Fact: {fact}"
'''