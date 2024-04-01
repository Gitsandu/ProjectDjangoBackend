from rest_framework.views import APIView
from Application.Service.UserService import UserService
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user_service = UserService()
        response = user_service.get_users(user_id)
        print('response', response)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    def post(self, request, *args, **kwargs):
        user_request_data = request.data 
        user_service = UserService()
        response = user_service.create_async(user_request_data)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)


    def put(self, request, *args, **kwargs):
        user_request_data = request.data 
        user_service = UserService()
        response = user_service.update_async(user_request_data)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        
        return Response(response_data)
    
    def delete(self, request, ids, *args, **kwargs):
        print('user ids: ', ids)
        user_service = UserService()
        user_ids = [int(user_id) for user_id in ids.split(',')]
        print('user_ids', user_ids)
        response = user_service.delete_async(user_ids)
        return response
    