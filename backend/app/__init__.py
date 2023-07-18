from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuración de la aplicación
    app.config['SECRET_KEY'] = 'citraditboard2023'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:citraditboard2023@localhost:5432/sgrdev'

    # Importa y registra los blueprints
    from app.admin.routes import admin_bp
    from app.auth.routes import auth_bp
    from app.interaction.routes import interaction_bp
    from app.support.routes import support_bp

    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(interaction_bp)
    app.register_blueprint(support_bp)

    # Inicializa las extensiones y configuraciones adicionales
    from app.extensions import db, migrate

    db.init_app(app)
    migrate.init_app(app, db)

    return app

app = create_app()
