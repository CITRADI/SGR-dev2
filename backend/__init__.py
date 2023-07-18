from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import db, login_manager, migrate

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(Config)

    # Inicialización de extensiones
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Importa los blueprints de los diferentes módulos
    from .auth.routes import auth_bp
    from .interaction.routes import interaction_bp
    from .admin.routes import admin_bp
    from .support.routes import support_bp

    # Registra los blueprints en la aplicación
    app.register_blueprint(auth_bp)
    app.register_blueprint(interaction_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(support_bp)

    return app

app = create_app()
