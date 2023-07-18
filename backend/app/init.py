from flask import Flask
from flask_cors import CORS
from .config import Config

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)

from backend.auth.routes import auth_bp
from backend.interaction.routes import interaction_bp
from backend.admin.routes import admin_bp
from backend.support.routes import support_bp

app.register_blueprint(auth_bp)
app.register_blueprint(interaction_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(support_bp)
