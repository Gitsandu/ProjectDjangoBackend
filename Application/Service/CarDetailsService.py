from Infrastructure.Repository.Repository import Repository
from  Core.Models.CarDetails import CarDetails
from automapper import mapper
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from typing import List, Type
from django.db import IntegrityError
from Application.Interface.CarDetailsAbstractService import CarDetailsAbstractService
from Application.Dto.CarDetails.CarDetailsRequest import CarDetailsRequest
from Application.Dto.CarDetails.CarDetailsResponse import CarDetailsResponse
from WebAPI.Serializers.CarDetails.CarDetailsRequestSeriliazer import CarDetailsRequestSeriliazer
from WebAPI.Serializers.CarDetails.CarDetailsResponseSeriliazer import CarDetialsResponseSerializer
from Application.Dto.EntityResponse.EntityResponseModel import EntityResponseModel
from Application.Helpers.APIResponseHelper import APIResponseHelper
from  Core.Models.CarOverview import CarOverview


class CarDetailsService(CarDetailsAbstractService):
    entity_service = Repository()
    
    @staticmethod
    def get_details(cardetail_id=None):
        if cardetail_id is not None:
            return CarDetailsService.retrieve_detail(cardetail_id)
        else:
            return CarDetailsService.list_details()
    
    @staticmethod
    def list_details():
        cardetails = CarDetailsService.entity_service.get_all_async(CarDetails)
        
        serializer = CarDetialsResponseSerializer(cardetails, many=True)
        cardetails_data = serializer.data
        
        print('cardetails_data', cardetails_data)
        mapped_cardetails = []
        
        for cardetail_data in cardetails_data:
            print('cardetail_data', cardetail_data)
            
            mapped_cardetail = mapper.to(CarDetailsResponse).map(cardetail_data)
            
            mapped_cardetails.append(vars(mapped_cardetail))
        
        EntityResponse = mapped_cardetails
        apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
        return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            
        # return Response(mapped_s, status=status.HTTP_200_OK)

    @staticmethod
    def retrieve_detail(cardetail_id):
        cardetail = CarDetailsService.entity_service.get_by_id_async(CarDetails, cardetail_id)
        
        if cardetail is not None:
            cardetail_info = mapper.to(CarDetailsResponse).map(cardetail)
            
            serializer = CarDetialsResponseSerializer(cardetail_info)
            response = serializer.data
            
            EntityResponse = response
            apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
            return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
        else:
            return Response({'error': 'CarDetail not found.'}, status=status.HTTP_404_NOT_FOUND)
        
    @staticmethod
    def create_async(model: Type[CarDetailsRequest]) -> CarDetails:
        serialized_data = CarDetailsRequestSeriliazer(data=model)
        print('serialized_data', serialized_data)
        if serialized_data.is_valid():
            cardetail_data = serialized_data.validated_data
            print('cardetail_data', cardetail_data)
            
            cardetail_data.pop('id', None)
            try:
                created_cardetails= CarDetailsService.entity_service.create_async(CarDetails,**cardetail_data)
                overview_data = {
                    'is_active': False,
                    'Location': cardetail_data['Location'],
                    'Brand_Name': cardetail_data['Brand_Name'],
                    'Model_Name': cardetail_data['Model_Name'],
                    'Variant_Name': cardetail_data['Variant_Name'],
                    'MFD_Year': cardetail_data['MFD_Year'],
                    'KiloMeter': cardetail_data['KiloMeter'],
                    'Ownership': cardetail_data['Ownership'],
                    'When_ToSell': cardetail_data['When_ToSell'],
                    'User': cardetail_data['User'],
                    'FuelType':cardetail_data['FuelType'],
                    'Transmission':cardetail_data['Transmission'],
                    'Seats':0,
                    'Price': 'verification needed',  # Set default value for new fields
                    'Insurance': 'verification needed',  # Set default value for new fields
                    'EngineCapacity': 'verification needed',
                    'Image':'verification needed'# Set default value for new fields
                }
                created_overview = CarDetailsService.entity_service.create_async(CarOverview, **overview_data)
                print('created_overview: ', created_overview)
                
                cardetail_info = mapper.to(CarDetailsResponse).map(created_cardetails)
                print('cardetail_info', cardetail_info)
                
                response_serializer = CarDetialsResponseSerializer(cardetail_info)
                
                response = response_serializer.data
                
                EntityResponse = response
                print('EntityResponse', EntityResponse)
                apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
                return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            except IntegrityError:
                return Response({'error': 'CarDetail creation failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            print('entered Else')
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @staticmethod   
    def update_async(updatemodel: Type[CarDetailsRequest]) -> CarDetails:
        
        update_serialized_data = CarDetailsRequestSeriliazer( data=updatemodel)
        if update_serialized_data.is_valid():
            
            update_cardetail_data = update_serialized_data.validated_data
            print('update_cardetail_data', update_cardetail_data)
            try:
                
                updated_cardetails = CarDetailsService.entity_service.update_async(CarDetails, update_cardetail_data)
                
                overview_data = {
                    'is_active': 'false',
                    'Location': update_cardetail_data['Location'],
                    'Brand_Name': update_cardetail_data['Brand_Name'],
                    'Model_Name': update_cardetail_data['Model_Name'],
                    'Variant_Name': update_cardetail_data['Variant_Name'],
                    'MFD_Year': update_cardetail_data['MFD_Year'],
                    'KiloMeter': update_cardetail_data['KiloMeter'],
                    'Ownership': update_cardetail_data['Ownership'],
                    'When_ToSell': update_cardetail_data['When_ToSell'],
                    'User': update_cardetail_data['User'],
                    'FuelType':update_cardetail_data['FuelType'],
                    'Transmission':update_cardetail_data['Transmission'],
                    'Seats':0,
                    'Price': 'verfication needed',  # Set default value for new fields
                    'Insurance': 'verification needed',  # Set default value for new fields
                    'EngineCapacity': 'verification needed',  # Set default value for new fields
                    'Image': 'verification needed'
                }
                
                carOwerview = CarOverview.objects.filter(id=updated_cardetails.id).update(**overview_data)
                print('carOwerview', carOwerview)
                
                updated_cardetail_info = mapper.to(CarDetailsResponse).map(updated_cardetails)
                
                response_serializer = CarDetialsResponseSerializer(updated_cardetail_info)
                
                response = response_serializer.data
                
                EntityResponse = response
                apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
                return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            except IntegrityError:
                return Response({'error': 'CarDetail creation failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            print('entered Else')
            return Response(update_serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @staticmethod    
    def delete_async(ids: List[int]) -> bool:
        print('ids :', ids)
        try:
            deleted_count = CarDetailsService.entity_service.delete_async(CarDetails, ids)
            secondDeleted_count = CarDetailsService.entity_service.delete_async(CarOverview, ids)
            if deleted_count > 0 or secondDeleted_count > 0:
                return Response({'success': f'{deleted_count + secondDeleted_count} cardetail(s) deleted successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'No cardetails were deleted.'}, status=status.HTTP_404_NOT_FOUND)

        except Http404:
            return Response({'error': 'cardetails not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Deletion failed. {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)