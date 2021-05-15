#This bluepint will deal with all user management functionality 

from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

from . import views