"""
blueprint creation for the home page
"""
from flask import Blueprint, render_template

home_bp= Blueprint('home_bp', __name__, template_folder='templates', static_folder='static')

@home_bp.route('/home')
def homepage():
    return render_template('home_base.html')
