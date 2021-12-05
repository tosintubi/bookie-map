import os
import logging

from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv

from src.models import db
from src.google import google_bp
from src.manage import create_tables

load_dotenv()


def create_app(test_config=None):
    app: Flask = Flask(__name__, instance_relative_config=True)
    
    if  not test_config:
        # Heroku Postgrseql hack.
        db_url = str(os.environ.get('DATABASE_URL'))
        if db_url.startswith('postgres://'):
            db_url = db_url.replace('postgres://', 'postgresql://',1)
        
        SECRET_KEY = os.environ.get('SECRET_KEY')
        if not SECRET_KEY:
            return 'secret key is missing'
        
        app.config.from_mapping(
            SECRET_KEY=os.environ.get('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=db_url,
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JSON_SORT_KEYS=False
        )
    else:
       app.config.from_mapping(test_config)

       
    # Initializations
    db.app = app
    db.init_app(app)
    migrate = Migrate(app,db)

    # Register blueprints
    app.register_blueprint(google_bp)
    
    #create table commands
    app.cli.add_command(create_tables)
    return app
