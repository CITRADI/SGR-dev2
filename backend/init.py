from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'tu_llave_secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:password@localhost/nombre_db'

    db.init_app(app)

    # Importar y registrar blueprints
    from .auth.routes import auth
    from .interaction.routes import interaction
    from .admin.routes import admin
    from .support.routes import support

    app.register_blueprint(auth)
    app.register_blueprint(interaction)
    app.register_blueprint(admin)
    app.register_blueprint(support)

    return app
