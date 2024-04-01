# from rest_framework.views import APIView
# from Application.Service.AuthUserService import AuthUserService
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

# class AuthUserView(APIView):
    
#     def get(self, request, *args, **kwargs):
#         user_id = kwargs.get('id')
#         user_service = AuthUserService()
#         response = user_service.get_users(user_id)
#         response_data = {
#             'statuscode': response.APIResponse.status_code,
#             'data': response.APIResponse.data,
#             'message': response.APIResponse.message,
#             'totalPages': response.APIResponse.totalPages,
#             'totalCount': response.APIResponse.totalCount
#         }
#         return Response(response_data)
    
#     def post(self, request, *args, **kwargs):
#         user_request_data = request.data 
#         print('user_request_data', user_request_data)
#         user_service = AuthUserService()
#         response = user_service.create_async(user_request_data)
#         print('response', response)
#         response_data = {
#             'statuscode': response.APIResponse.status_code,
#             'data': response.APIResponse.data,
#             'message': response.APIResponse.message,
#             'totalPages': response.APIResponse.totalPages,
#             'totalCount': response.APIResponse.totalCount
#         }
#         return Response(response_data)


#     def put(self, request, *args, **kwargs):
#         user_request_data = request.data 
#         user_service = AuthUserService()
#         response = user_service.update_async(user_request_data)
#         response_data = {
#             'statuscode': response.APIResponse.status_code,
#             'data': response.APIResponse.data,
#             'message': response.APIResponse.message,
#             'totalPages': response.APIResponse.totalPages,
#             'totalCount': response.APIResponse.totalCount
#         }
        
#         return Response(response_data)
    
#     def delete(self, request, ids, *args, **kwargs):
#         print('user ids: ', ids)
#         user_service = AuthUserService()
#         user_ids = [int(user_id) for user_id in ids.split(',')]
#         print('user_ids', user_ids)
#         response = user_service.delete_async(user_ids)
#         return response


from django.http.response import JsonResponse
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from Application.Dto.APIResponse.APIResponse import APIResponse
from Application.Service.AuthUserService import AuthUserService
from drf_yasg.utils import swagger_auto_schema
from WebAPI.Serializers.AuthUser.AuthUserRequestSerializer import AuthUserRequestSerializer

class AuthUserViewSet(ViewSet):
    
    def list(self, request):
        user_service = AuthUserService()
        response = user_service.get_users()
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    def retrieve(self, request, pk=None):
        user_service = AuthUserService()
        response = user_service.get_users(pk)
        response_data = response.APIResponse
        return Response(response_data.to_dict()) 
    
    @swagger_auto_schema(request_body=AuthUserRequestSerializer)
    def create(self, request):
        user_request_data = request.data 
        
        print('user_request_data', user_request_data)
        user_service = AuthUserService()
        response = user_service.create_async(user_request_data)
        print('response', response)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    @swagger_auto_schema(request_body=AuthUserRequestSerializer)
    def update(self, request, *args, **kwargs):
        user_request_data = request.data 
        user_service = AuthUserService()
        response = user_service.update_async(user_request_data)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    def destroy(self, request, pk=None):
        print('user id: ', pk)
        user_service = AuthUserService()
        response = user_service.delete_async(pk)
        return response