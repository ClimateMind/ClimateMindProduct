from flask import Flask
from flask_selfdoc import Autodoc
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

from config import DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = "auth.login"
login.login_message = "Please log in to access this page."
cache = Cache()
auto = Autodoc()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    cache.init_app(app)
    auto.init_app(app)
    CORS(app)

    with app.app_context():

        from app.errors import bp as errors_bp

        app.register_blueprint(errors_bp)

        from app.subscribe import bp as subscribe_bp

        app.register_blueprint(subscribe_bp)

        from app.feed import bp as feed_bp

        app.register_blueprint(feed_bp)

        from app.myths import bp as myths_bp

        app.register_blueprint(myths_bp)

        from app.solutions import bp as solutions_bp

        app.register_blueprint(solutions_bp)

        from app.scoring import bp as scoring_bp

        app.register_blueprint(scoring_bp)

        from app.questions import bp as questions_bp

        app.register_blueprint(questions_bp)

        from app.personal_values import bp as personal_values_bp

        app.register_blueprint(personal_values_bp)

        from app.documentation import bp as documentation_bp

        app.register_blueprint(documentation_bp)

        from app.post_code import bp as post_code_bp

        app.register_blueprint(post_code_bp)

    return app


from app import models
