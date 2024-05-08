from flask import (Blueprint, render_template)

bp = Blueprint('pet', __name__, url_prefix="/pwts/pet")

@bp.route('/')
def index():
    return render_template('index.html')