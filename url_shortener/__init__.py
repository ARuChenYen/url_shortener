from flask import Flask
from .extensions import db
from .route import short

def create_app(config_file='setting.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)
    
    app.register_blueprint(short)

    return app
