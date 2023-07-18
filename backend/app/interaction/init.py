from flask import Blueprint

interaction_bp = Blueprint('interaction', __name__)

from interaction.routes import *
