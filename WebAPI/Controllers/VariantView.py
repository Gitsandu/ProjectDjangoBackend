from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from Application.Service.VariantService import VariantService
from drf_yasg.utils import swagger_auto_schema
from WebAPI.Serializers.Variant.CarVariantRequestSerializers import CarVariantRequestSerializer
from Application.Service.JWTAuthentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class VariantViewSet(ViewSet):
    # authentication_classes = [JWTAuthentication] 
    # permission_classes = [IsAuthenticated] 

    def list(self, request):
        variant_service = VariantService()
        response = variant_service.get_variants()
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    def retrieve(self, request, pk=None):
        varinat_service = VariantService()
        response = varinat_service.get_variants(pk)
        
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    @swagger_auto_schema(request_body=CarVariantRequestSerializer)
    def create(self, request):
        variant_request_data = request.data 
        print('variant_request_data', variant_request_data)
        variant_service = VariantService()
        response = variant_service.create_async(variant_request_data)
        print('response', response)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    @swagger_auto_schema(request_body=CarVariantRequestSerializer)
    def update(self, request, *args, **kwargs):
        variant_request_data = request.data 
        variant_service = VariantService()
        response = variant_service.update_async(variant_request_data)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    def destroy(self, request, pk=None):
        print('variant id: ', pk)
        variant_service = VariantService()
        response = variant_service.delete_async(pk)
        return response