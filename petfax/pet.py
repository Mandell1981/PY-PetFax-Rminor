from flask import (Blueprint, render_template, request)
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

#index route
@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

#show route
@bp.route('/pets/<int:index>')
def show(index):
    pet = pets[index]
    return render_template('show.html', pet=pet)

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
