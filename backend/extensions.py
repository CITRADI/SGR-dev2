from flask_migrate import Migrate
from flask_login import LoginManager

migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
