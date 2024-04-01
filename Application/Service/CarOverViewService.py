from Infrastructure.Repository.Repository import Repository
from automapper import mapper
from rest_framework import status
from rest_framework.response import Response
from Application.Interface.CarOverViewAbstractService import CarOverViewAbstractService
from Application.Dto.CarOverView.CarOverViewResponse import CarOverViewResponse
from WebAPI.Serializers.CarOverVIew.CarOverViewResponseSerializer import CarOverViewResponseSerializer
from Application.Dto.EntityResponse.EntityResponseModel import EntityResponseModel
from Application.Helpers.APIResponseHelper import APIResponseHelper
from  Core.Models.CarOverview import CarOverview

class CarOverviewService(CarOverViewAbstractService):
    entity_service = Repository()
    
    @staticmethod
    def get_details(cardetail_id=None):
        if cardetail_id is not None:
            return CarOverviewService.retrieve_detail(cardetail_id)
        else:
            return CarOverviewService.list_details()
    
    @staticmethod
    def list_details():
        cardetails = CarOverviewService.entity_service.get_all_async(CarOverview)
        print('cardetails', cardetails)
        
        serializer = CarOverViewResponseSerializer(cardetails, many=True)
        cardetails_data = serializer.data
        
        print('cardetails_data', cardetails_data)
        mapped_cardetails = []
        
        for cardetail_data in cardetails_data:
            print('cardetail_data', cardetail_data)
            
            mapped_cardetail = mapper.to(CarOverViewResponse).map(cardetail_data)
            
            mapped_cardetails.append(vars(mapped_cardetail))
        
        EntityResponse = mapped_cardetails
        apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
        return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
    

    @staticmethod
    def retrieve_detail(cardetail_id):
        cardetail = CarOverviewService.entity_service.get_by_id_async(CarOverview, cardetail_id)
        print('cardetail', cardetail)
        
        if cardetail is not None:
            cardetail_info = mapper.to(CarOverViewResponse).map(cardetail)
            
            serializer = CarOverViewResponseSerializer(cardetail_info)
            response = serializer.data
            
            EntityResponse = response
            apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
            return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
        else:
            return Response({'error': 'CarDetail not found.'}, status=status.HTTP_404_NOT_FOUND)