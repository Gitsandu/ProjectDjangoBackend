from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from Application.Service.CarDetailsService import CarDetailsService
from drf_yasg.utils import swagger_auto_schema
from WebAPI.Serializers.CarDetails.CarDetailsRequestSeriliazer import CarDetailsRequestSeriliazer
from Application.Service.JWTAuthentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class CarDetailsViewSet(ViewSet):

    def list(self, request):
        cardetail_service = CarDetailsService()
        response = cardetail_service.get_details()
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    def retrieve(self, request, pk=None):
        cardetail_service = CarDetailsService()
        response = cardetail_service.get_details(pk)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    @swagger_auto_schema(request_body=CarDetailsRequestSeriliazer)
    def create(self, request):
        cardetail_request_data = request.data 
        print('cardetail_request_data', cardetail_request_data)
        cardetail_service = CarDetailsService()
        response = cardetail_service.create_async(cardetail_request_data)
        print('response', response)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    @swagger_auto_schema(request_body=CarDetailsRequestSeriliazer)
    def update(self, request, *args, **kwargs):
        cardetail_request_data = request.data 
        cardetail_service = CarDetailsService()
        response = cardetail_service.update_async(cardetail_request_data)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    def destroy(self, request, pk=None):
        print('cardetail id: ', pk)
        cardetail_service = CarDetailsService()
        response = cardetail_service.delete_async(pk)
        return response