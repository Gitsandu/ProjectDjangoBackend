from Infrastructure.Repository.Repository import Repository
from automapper import mapper
from rest_framework import status
from rest_framework.response import Response
from Application.Interface.CarImageAbstractServices import CarImageAbstractService
from Application.Dto.CarImage.CarImageResponse import CarImageResponse
from WebAPI.Serializers.CarImages.CarImageResponseSerializer import CarImageResponseSerializer
from Application.Dto.EntityResponse.EntityResponseModel import EntityResponseModel
from Application.Helpers.APIResponseHelper import APIResponseHelper
from  Core.Models.CarImage import CarImage

class CarImageService(CarImageAbstractService):
    entity_service = Repository()
    
    @staticmethod
    def get_details(carimage_id=None):
        if carimage_id is not None:
            return CarImageService.retrieve_detail(carimage_id)
        else:
            return CarImageService.list_details()
    
    @staticmethod
    def list_details():
        carimages = CarImageService.entity_service.get_all_async(CarImage)
        print('carimages', carimages)

        serializer = CarImageResponseSerializer(carimages, many=True)
        carImage_datas = serializer.data
        print('carimages', carimages)
        mapped_carimages = []
        
        for carImage_data in carImage_datas:
            print('carimages', carimages)

            mapped_carimage = mapper.to(CarImageResponse).map(carImage_data)
            print('carimages', carimages)

            mapped_carimages.append(vars(mapped_carimage))

        
        EntityResponse = mapped_carimages
        apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
        return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
    

    @staticmethod
    def retrieve_detail(carimage_id):
        carimage = CarImageService.entity_service.get_by_id_async(CarImage, carimage_id)
        
        if carimage is not None:
            carimage_info = mapper.to(CarImageResponse).map(carimage)
            
            serializer = CarImageResponseSerializer(carimage_info)
            response = serializer.data
            
            EntityResponse = response
            apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
            return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
        else:
            return Response({'error': 'CarImage not found.'}, status=status.HTTP_404_NOT_FOUND)
