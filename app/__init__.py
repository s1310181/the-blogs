from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-secret-change-in-production"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blogs.db"

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from app.models import User, Post  # noqa: F401

    with app.app_context():
        db.create_all()

    from app.routes import bp as main_bp
    from app.auth import bp as auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app
