from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .TokenService import TokenService 

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        print('request', request.headers)
        token = request.headers.get('Authorization')  
        print('token', token)
        if not token:
            return None
        try:
            user = TokenService().validate_token(token) 
            print('user', user)
        except Exception as e:
            raise AuthenticationFailed('Invalid or expired token.')
        
        if not user:
            raise AuthenticationFailed('User not found.')
        
        return (user, None)