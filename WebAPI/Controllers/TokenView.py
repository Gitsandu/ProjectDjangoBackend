from rest_framework.response import Response
from Application.Service.TokenService import TokenService
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from WebAPI.Serializers.Token.TokenSerializer import TokenSerializer
from WebAPI.Serializers.Token.TokenPasswordSerlizer import TokenPasswordSerlizer
from rest_framework import status

class TokenView(ViewSet):
    @swagger_auto_schema(request_body=TokenSerializer)
    def create(self, request):
        user_request_data = request.data 
        print('user_request_data', user_request_data)
        token_service = TokenService()
        response = token_service.generate_auth_token(user_request_data)
        print('response', response)
        return Response(response)

class TokenValidationViewSet(ViewSet):
    @swagger_auto_schema(request_body=TokenPasswordSerlizer)
    def create(self, request):
        token = request.data.get('token')
        if not token:
            return Response({'error': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)
        token_service = TokenService()
        user = token_service.validate_token(token)
        if user is not None:
            return Response({'valid': True, 'user_id': user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'valid': False}, status=status.HTTP_401_UNAUTHORIZED)
    
    
    

    # def post(self, request):
    #     user_request_data = request.data 
    #     print('user_request_data', user_request_data)
    #     tokenService =TokenService()
    #     response = tokenService.generate_auth_token(user_request_data)
    #     print('response', response)
    #     return Response(response)