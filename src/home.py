
from google.auth import jwt
from flask import Blueprint, jsonify, request

home = Blueprint('home', __name__, url_prefix='/')


@home.get('home')
def hello():
    return jsonify({'hello':'world'})
