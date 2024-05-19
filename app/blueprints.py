# Import the flask Blueprint to allow for multiple configs
from flask import Blueprint

# Creating main for route
main = Blueprint('main',__name__)

from app import models, routes, api