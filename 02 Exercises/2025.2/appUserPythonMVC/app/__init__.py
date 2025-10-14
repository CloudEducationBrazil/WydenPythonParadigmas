from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # <- aqui aponta para config.py dentro da pasta app

    db.init_app(app)

    from app.controllers.UserController import user_bp
    app.register_blueprint(user_bp)

    return app