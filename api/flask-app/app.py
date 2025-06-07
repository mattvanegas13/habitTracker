from flask import Flask
from flask_cors import CORS
from .routes import healthCheck, habits
from .models import db

def create_app(config_file='config.py'):
    """Factory to create the Flask application
    :return: A `Flask` application instance
    """
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    _register_blueprints(app)
    CORS(app)
    return app


def _register_blueprints(app):
    app.register_blueprint(healthCheck.health_bp, url_prefix='/health')
    app.register_blueprint(habits.habits_bp, url_prefix='/habits')
    
if __name__ == '__main__':
    app = create_app()
    app.run()