import uuid
import logging
from datetime import datetime

from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash
import validators

from src.models import UserLogin, UserProfile, db
from src.google import get_user_info
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
        
    # Check the length of the username.
    
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
    
    return jsonify(get_user_info(new_user.id)), HTTP_201_CREATED

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
        return jsonify(get_user_info(usr.id)), HTTP_200_OK
    
    return jsonify({'error':'incorrect password'}), HTTP_401_UNAUTHORIZED
