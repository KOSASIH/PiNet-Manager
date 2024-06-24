# security.py
import jwt
from flask_jwt_extended import JWTManager
from oauthlib.oauth2 import WebApplicationClient

jwt_manager = JWTManager()

# Generate JWT token
def generate_token(user_id):
    payload = {'user_id': user_id}
    token = jwt.encode(payload, 'secret_key', algorithm='HS256')
    return token

# OAuth2 client
oauth_client = WebApplicationClient('client_id', 'client_secret')

# Authenticate with OAuth2
def authenticate_with_oauth2():
    auth_url = oauth_client.prepare_request_uri('https://example.com/oauth2/authorize')
    return auth_url

# Verify JWT token
def verify_token(token):
    try:
        payload = jwt.decode(token, 'secret_key', algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
