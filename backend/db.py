from flask_sqlalchemy import SQLAlchemy

# Crea una instancia del objeto SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    # Configura la base de datos con la aplicación Flask
    db.init_app(app)
    # Realiza la creación de las tablas en la base de datos
    with app.app_context():
        db.create_all()
        # Puedes agregar aquí otras operaciones iniciales si es necesario

def close_db():
    # Cierra la conexión con la base de datos
    db.session.close()
