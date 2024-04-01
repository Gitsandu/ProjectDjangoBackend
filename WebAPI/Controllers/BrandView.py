from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from Application.Service.BrandService import BrandService
from drf_yasg.utils import swagger_auto_schema
from WebAPI.Serializers.Brand.BrandRequestSerializer import BrandRequestSerializer
from Application.Service.JWTAuthentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class BrandViewSet(ViewSet):
    # authentication_classes = [JWTAuthentication] 
    # permission_classes = [IsAuthenticated] 


    def list(self, request):
        brand_service = BrandService()
        response = brand_service.get_brands()
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    def retrieve(self, request, pk=None):
        brand_service = BrandService()
        response = brand_service.get_brands(pk)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    @swagger_auto_schema(request_body=BrandRequestSerializer)
    def create(self, request):
        brand_request_data = request.data 
        print('brand_request_data', brand_request_data)
        brand_service = BrandService()
        response = brand_service.create_async(brand_request_data)
        print('response', response)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    @swagger_auto_schema(request_body=BrandRequestSerializer)
    def update(self, request, *args, **kwargs):
        brand_request_data = request.data 
        brand_service = BrandService()
        response = brand_service.update_async(brand_request_data)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    def destroy(self, request, pk=None):
        print('brand id: ', pk)
        brand_service = BrandService()
        response = brand_service.delete_async(pk)
        return response