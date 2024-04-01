from Infrastructure.Repository.Repository import Repository
from Core.Models.Location import Location
from automapper import mapper
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from typing import List, Type
from django.db import IntegrityError
from Application.Interface.LocationAbstractService import LocationAbstractService
from Application.Dto.Location.LocationRequest import LocationRequest
from Application.Dto.Location.LocationResponse import LocationResponse
from WebAPI.Serializers.Location.LocationRequestSerializer import LocationRequestSerializer
from WebAPI.Serializers.Location.LocationResponseSerializer import LocationResponseSerializer
from Application.Dto.EntityResponse.EntityResponseModel import EntityResponseModel
from Application.Helpers.APIResponseHelper import APIResponseHelper

class LocationService(LocationAbstractService):
    entity_service = Repository()
    
    @staticmethod
    def get_locations(location_id=None):
        if location_id is not None:
            return LocationService.retrieve_location(location_id)
        else:
            return LocationService.list_locations()
    
    @staticmethod
    def list_locations():
        locations = LocationService.entity_service.get_all_async(Location)
        
        serializer = LocationResponseSerializer(locations, many=True)
        locations_data = serializer.data
        
        mapped_locations = []
        
        for location_data in locations_data:
            location = Location(**location_data)
            
            mapped_location = mapper.to(LocationResponse).map(location)
            
            mapped_locations.append(vars(mapped_location))
        
        EntityResponse = mapped_locations
        apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
        return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            
        # return Response(mapped_users, status=status.HTTP_200_OK)

    @staticmethod
    def retrieve_location(location_id):
        location = LocationService.entity_service.get_by_id_async(Location, location_id)
        
        if location is not None:
            location_info = mapper.to(LocationResponse).map(location)
            
            serializer = LocationResponseSerializer(location_info)
            response = serializer.data
            
            EntityResponse = response
            apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
            return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
        else:
            return Response({'error': 'Location not found.'}, status=status.HTTP_404_NOT_FOUND)
        
    @staticmethod
    def create_async(model: Type[LocationRequest]) -> Location:
        serialized_data = LocationRequestSerializer(data=model)
        
        if serialized_data.is_valid():
            location_data = serialized_data.validated_data
            location_data.pop('id', None)
            try:
                
                created_locations = LocationService.entity_service.create_async(Location,**location_data)
                
                location_info = mapper.to(LocationResponse).map(created_locations)
                
                response_serializer = LocationResponseSerializer(location_info)
                
                response = response_serializer.data
                
                EntityResponse = response
                apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
                return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            except IntegrityError:
                return Response({'error': 'Location creation failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            print('entered Else')
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @staticmethod   
    def update_async(updatemodel: Type[LocationRequest]) -> Location:
        
        update_serialized_data = LocationRequestSerializer( data=updatemodel)
        if update_serialized_data.is_valid():
            
            update_location_data = update_serialized_data.validated_data
            try:
                updated_locations = LocationService.entity_service.update_async(Location, update_location_data)

                updated_location_info = mapper.to(LocationResponse).map(updated_locations)
                
                response_serializer = LocationResponseSerializer(updated_location_info)
                
                response = response_serializer.data
                
                EntityResponse = response
                apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
                return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            except IntegrityError:
                return Response({'error': 'Location creation failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            print('entered Else')
            return Response(update_serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @staticmethod    
    def delete_async(ids: List[int]) -> bool:
        print('ids :', ids)
        try:
            deleted_count = LocationService.entity_service.delete_async(Location, ids)
            if deleted_count > 0:
                return Response({'success': f'{deleted_count} location(s) deleted successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'No locations were deleted.'}, status=status.HTTP_404_NOT_FOUND)

        except Http404:
            return Response({'error': 'Location not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Deletion failed. {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)