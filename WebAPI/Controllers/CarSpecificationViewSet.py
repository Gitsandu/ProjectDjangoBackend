from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from Application.Service.CarSpecificationService import CarSpecificationService
from Application.Service.JWTAuthentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class CarSpecificationViewSet(ViewSet):

    def list(self, request):
        cardetail_service = CarSpecificationService()
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
        cardetail_service = CarSpecificationService()
        response = cardetail_service.get_details(pk)
        response_data = {
            'statuscode': response.APIResponse.status_code,
            'data': response.APIResponse.data,
            'message': response.APIResponse.message,
            'totalPages': response.APIResponse.totalPages,
            'totalCount': response.APIResponse.totalCount
        }
        return Response(response_data)