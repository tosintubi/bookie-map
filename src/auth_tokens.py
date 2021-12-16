from flask_jwt_extended.utils import create_access_token, create_refresh_token


def create_auth_tokens(id):
    
    # Create refresh  and accss token
    refresh_token = create_refresh_token(identity=id)
    access_token = create_access_token(identity=id)
    
    auth_tokens = {
        'refresh': refresh_token,
        'access': access_token
    }
    return auth_tokens
        
