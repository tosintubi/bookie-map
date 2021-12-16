from os import access
import uuid
import logging
from datetime import datetime

from flask_jwt_extended.utils import get_jwt_identity

import validators
from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token

from src.models import UserLogin, UserProfile, db
from src.google import get_user_info
from src.auth_tokens import create_auth_tokens
from src.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLIT



user_bp = Blueprint('user', __name__, url_prefix='/api')

@user_bp.post('/login/user/signup')
def signup():
    """Endpoint for user signup

    Returns:
        json: user's information
    """
    
    if 'first_name' not in request.json:
        return jsonify({
            'error': "'first_name' is missing from request"
        }), HTTP_400_BAD_REQUEST
        
    if 'last_name' not in request.json:
        return jsonify({
            'error': "'last_name' is missing from request"
        }), HTTP_400_BAD_REQUEST
    
    if 'email' not in request.json:
        return jsonify({
            'error': "'email' is missing from request"
        }), HTTP_400_BAD_REQUEST
    
    if 'password' not in request.json:
        return jsonify({
            'error': "'password' is missing from request"
        }), HTTP_400_BAD_REQUEST
        
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    password = request.json['password']
    
    if len(password) < 8:
        return jsonify({
            'error': "'password' is too short"
        }), HTTP_400_BAD_REQUEST
    
    if not validators.email(email):
        return jsonify({
            'error': "'email' is invalid"
        }), HTTP_400_BAD_REQUEST
        
    # Check if email is taken    
    if UserProfile.query.filter_by(email=email).first() is not None:
        return jsonify({
            'error': "'email' is already taken"
        }), HTTP_409_CONFLIT
        
    password_hash = generate_password_hash(password)
    
    new_user = UserProfile(
        id=uuid.uuid4(),
        first_name=first_name,
        last_name=last_name,
        email=email,
    )
    # user Login
    user_login = UserLogin(
        id=uuid.uuid4(),
        google_login=True,
        is_active=True,
        password_hash=password_hash,
        user_profile_id=new_user.id,
        last_login=datetime.now()
    )

    db.session.add(new_user)
    db.session.add(user_login)
    db.session.commit()
    
    user_info = get_user_info(new_user.id)
        
    # creates access & refresh tokens and append it to user_info object
    tokens = create_auth_tokens(new_user.id)      
    user_info.update({'tokens':tokens})
    
    return jsonify(user_info), HTTP_201_CREATED

@user_bp.post('/login/user')
def login():
    """Login endpoint

    Returns:
        json: user's information
    """
    
    if 'email' not in request.json:
        return jsonify({
            'error': "'email' cannot be blank"
        }), HTTP_400_BAD_REQUEST
        
    if 'password' not in request.json:
        return jsonify({
            'error': "'password cannot be blank' is missing"
        }), HTTP_400_BAD_REQUEST
    
    email = request.json['email']
    password = request.json['password']
    
    if not validators.email(email):
        return jsonify({
            'error': "'email' is invalid"
        }), HTTP_400_BAD_REQUEST

    # check if user exists
    usr = UserProfile.query.filter_by(email=email).first()
    if not usr:
        return jsonify({
            'error': "'user' is invalid"
        }), HTTP_401_UNAUTHORIZED
    
    user_login = UserLogin.query.filter_by(user_profile_id=usr.id).first()
    
    
    # Check if password is correct
    is_valid_pass = check_password_hash(
        pwhash=user_login.password_hash,
        password=password)
    if is_valid_pass:
        
        
        user_info =  get_user_info(usr.id)
        
        # creates access & refresh tokens and append it to user_info object
        tokens = create_auth_tokens(usr.id)      
        user_info.update({'tokens':tokens})
        
        # updates last login
        user_login.last_login = datetime.now()    
        db.session.commit()
        
        return jsonify(user_info), HTTP_200_OK
    
    return jsonify({'error':'incorrect password'}), HTTP_401_UNAUTHORIZED

@user_bp.get('/login/user/me')
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = UserProfile.query.filter_by(id=user_id).first()
    return jsonify({
        'name': user.first_name +" "+ user.last_name,
        'email': user.email
    }), HTTP_200_OK
