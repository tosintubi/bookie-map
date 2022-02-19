import os
import json
from datetime import timedelta

from flask import Flask
from flask.json import jsonify
from flask_jwt_extended.jwt_manager import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv
from flasgger import Swagger, swag_from
from src.constants.http_status_codes import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

from src.models import db
from src.google import google_bp
from src.user import user_bp
from src.manage import create_tables, drop_create, generate_data
from src.config.swagger import template,swagger_config

load_dotenv()

def get_db_url():
    # Heroku hack
    db_url = os.environ.get('DATABASE_URL')
    
    if db_url:       
        if db_url.startswith('postgres://'):
            db_url = db_url.replace('postgres://', 'postgresql://',1)
    return db_url
    

def create_app(test_config=None):
    app: Flask = Flask(__name__, instance_relative_config=True)
    
    secret_key = os.environ.get('SECRET_KEY')
    if  secret_key is None:
        raise Exception("SECRET_KEY does not exist")
    
    db_url = get_db_url()
    
    if db_url is None:
        raise Exception("DATABASE_URL does not exist")
    
    if  not test_config:
        app.config.from_mapping(
            SECRET_KEY=secret_key,
            SQLALCHEMY_DATABASE_URI=get_db_url(),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JSON_SORT_KEYS=False,
            SWAGGER={
                'title': 'Bookiemap P2P API',
                'uiversion':3
            },
            JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES'))),
            JWT_REFRESH_TOKEN_EXPIRES=timedelta(days=int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES')))
        )
    else:
       app.config.from_mapping(test_config)
       
    # Initializations.
    db.app = app
    db.init_app(app)
    migrate = Migrate(app,db)
    JWTManager(app)
    
    # Register blueprints
    app.register_blueprint(google_bp)
    app.register_blueprint(user_bp)
    
    #create table commands
    app.cli.add_command(create_tables)
    app.cli.add_command(drop_create)
    app.cli.add_command(generate_data)
    
    # swagger configuration
    Swagger(app=app, config=swagger_config,template=template)
    
    # error handling        
    @app.errorhandler(HTTP_404_NOT_FOUND)
    def handle_404(e):
        return jsonify({
            'error': 'Not found',
            'code':HTTP_404_NOT_FOUND
            }), HTTP_404_NOT_FOUND

    # Only works in PROD mode
    @app.errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
    def handle_500(e):
        return jsonify({
            'error': 'Something went wrong, we are working on it',
            'code':HTTP_500_INTERNAL_SERVER_ERROR
            }), HTTP_500_INTERNAL_SERVER_ERROR
        
    
    return app
