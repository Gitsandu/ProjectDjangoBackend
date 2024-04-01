from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from Application.Service.ModelService import ModelService
from drf_yasg.utils import swagger_auto_schema
from WebAPI.Serializers.Model.CarModelRequestSeriliazer import CarModelRequestSerializer
from Application.Service.JWTAuthentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class ModelViewSet(ViewSet):
    # authentication_classes = [JWTAuthentication] 
    # permission_classes = [IsAuthenticated] 

    def list(self, request):
        model_service = ModelService()
        response = model_service.get_models()
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    def retrieve(self, request, pk=None):
        model_service = ModelService()
        response = model_service.get_models(pk)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    @swagger_auto_schema(request_body=CarModelRequestSerializer)
    def create(self, request):
        model_request_data = request.data 
        print('model_request_data', model_request_data)
        model_service = ModelService()
        response = model_service.create_async(model_request_data)
        print('response', response)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    @swagger_auto_schema(request_body=CarModelRequestSerializer)
    def update(self, request, *args, **kwargs):
        model_request_data = request.data 
        model_service = ModelService()
        response = model_service.update_async(model_request_data)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    def destroy(self, request, pk=None):
        print('model id: ', pk)
        model_service = ModelService()
        response = model_service.delete_async(pk)
        return response