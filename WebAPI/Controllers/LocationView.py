from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from Application.Service.LocationService import LocationService
from drf_yasg.utils import swagger_auto_schema
from WebAPI.Serializers.Location.LocationRequestSerializer import LocationRequestSerializer
from Application.Service.JWTAuthentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class LocationViewSet(ViewSet):
    
    def list(self, request):
        location_service = LocationService()
        response = location_service.get_locations()
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    def retrieve(self, request, pk=None):
        location_service = LocationService()
        response = location_service.get_locations(pk)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    @swagger_auto_schema(request_body=LocationRequestSerializer)
    def create(self, request):
        location_request_data = request.data 
        print('location_request_data', location_request_data)
        location_service = LocationService()
        response = location_service.create_async(location_request_data)
        print('response', response)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    @swagger_auto_schema(request_body=LocationRequestSerializer)
    def update(self, request, *args, **kwargs):
        location_request_data = request.data 
        location_service = LocationService()
        response = location_service.update_async(location_request_data)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)
    
    def destroy(self, request, pk=None):
        print('location id: ', pk)
        location_service = LocationService()
        response = location_service.delete_async(pk)
        return response