from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .AuthUserService import AuthUserService
from WebAPI.Serializers.AuthUser.AuthUserResponseSerializer import AuthUserResponseSerializer
from Application.Dto.AuthUser.AuthUserResponse import AuthUserResponse
from automapper import mapper
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

class TokenService:
    auth_user = AuthUserService()
    
    def generate_auth_token(self, request):
        username = request.get('username')
        password = request.get('password')
        
        userbyname = TokenService.auth_user.retrieve_user_name(username)
        
        if userbyname is not None:
            serializer = AuthUserResponseSerializer(userbyname)
            response = serializer.data
            print('response', response)
            
            checkPass = response['password']
            
            if(check_password(password, checkPass)):
                user = authenticate(username=username, password=password)
                
                if user :
                    refresh = RefreshToken.for_user(user)
                    access_token = str(refresh.access_token)
                    refresh_token = str(refresh)
                    return {'access_token': access_token, 'refresh_token': refresh_token, 'response': response}
                
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    
    def validate_token(self, token):
        print('token in validate token', token)
        jwt_authentication = JWTAuthentication()
        validated_token = jwt_authentication.get_validated_token(token)
        print('validated_token', validated_token)
        user = jwt_authentication.get_user(validated_token)
        print('user', user)
        return user
            
# class TokenAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         auth_header = request.headers.get('Authorization')
        
#         if not auth_header:
#             return None
        
#         token = auth_header.split()[1] 
#         print('token in token class: ', token)
#         token_service = TokenService()
#         user = token_service.validate_token(token)
#         if user is None:
#             raise AuthenticationFailed('Invalid token.')
        
#         return (user, token)

