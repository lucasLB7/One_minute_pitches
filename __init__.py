from flask import flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_SQLAlchemy import flask_SQLAlchemy
from flask_login import LoginManager
from flask_mail import flask_mail
from flask_simplemde import SimpleMDE


bootstrap = Bootstrap()
db = SQLAlchemy()
LoginManager = LoginManager()
LoginManager.session_protection = 'Strong'
LoginManager.login_view = 'auth.login'
mail = Mail()
simple = SimpleMDE()


def create_app(config_name):
    app = Flask(__name__)


    app.config.from_object(config_options[config_name])


    bootstrap.init_app(app)
    db.init_app(app)
    LoginManager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/signin')

    return app
