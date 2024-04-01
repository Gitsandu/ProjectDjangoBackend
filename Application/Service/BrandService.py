from Infrastructure.Repository.Repository import Repository
from Core.Models.CarBrand import CarBrand
from automapper import mapper
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from typing import List, Type
from django.db import IntegrityError
from Application.Interface.CarBrandAbstractService import CarBrandAbstractService
from Application.Dto.Brand.CarBrandRequest import CarBrandRequest
from Application.Dto.Brand.CarBrandResponse import CarBrandResponse
from WebAPI.Serializers.Brand.BrandRequestSerializer import BrandRequestSerializer
from WebAPI.Serializers.Brand.BrandResponseSeriliazer import BrandResponseSerializer
from Application.Dto.EntityResponse.EntityResponseModel import EntityResponseModel
from Application.Helpers.APIResponseHelper import APIResponseHelper


class BrandService(CarBrandAbstractService):
    entity_service = Repository()
    
    @staticmethod
    def get_brands(brand_id=None):
        if brand_id is not None:
            return BrandService.retrieve_brand(brand_id)
        else:
            return BrandService.list_brands()
    
    @staticmethod
    def list_brands():
        brands = BrandService.entity_service.get_all_async(CarBrand)
        
        serializer = BrandResponseSerializer(brands, many=True)
        brands_data = serializer.data
        
        mapped_brands = []
        
        for brand_data in brands_data:
            brand = CarBrand(**brand_data)
            
            mapped_brand = mapper.to(CarBrandResponse).map(brand)
            
            mapped_brands.append(vars(mapped_brand))
        
        EntityResponse = mapped_brands
        apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
        return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            
        # return Response(mapped_users, status=status.HTTP_200_OK)

    @staticmethod
    def retrieve_brand(brand_id):
        brand = BrandService.entity_service.get_by_id_async(CarBrand, brand_id)
        
        if brand is not None:
            brand_info = mapper.to(CarBrandResponse).map(brand)
            
            serializer = BrandResponseSerializer(brand_info)
            response = serializer.data
            
            EntityResponse = response
            apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
            return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
        else:
            return Response({'error': 'Brand not found.'}, status=status.HTTP_404_NOT_FOUND)
        
    @staticmethod
    def create_async(model: Type[CarBrandRequest]) -> CarBrand:
        serialized_data = BrandRequestSerializer(data=model)
        
        if serialized_data.is_valid():
            brand_data = serialized_data.validated_data
            print('brand_data', brand_data)
            
            brand_data.pop('id', None)
            try:
                created_brands = BrandService.entity_service.create_async(CarBrand,**brand_data)
                
                brand_info = mapper.to(CarBrandResponse).map(created_brands)
                print('brand_info', brand_info)
                
                response_serializer = BrandResponseSerializer(brand_info)
                
                response = response_serializer.data
                
                EntityResponse = response
                print('EntityResponse', EntityResponse)
                apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
                return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            except IntegrityError:
                return Response({'error': 'Brand creation failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            print('entered Else')
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @staticmethod   
    def update_async(updatemodel: Type[CarBrandRequest]) -> CarBrand:
        
        update_serialized_data = BrandRequestSerializer( data=updatemodel)
        if update_serialized_data.is_valid():
            
            update_brand_data = update_serialized_data.validated_data
            print('update_brand_data', update_brand_data)
            try:
                update_brand_id = update_brand_data['id']
                print('update_brand_id', update_brand_id)
                
                updated_brands = BrandService.entity_service.update_async(CarBrand, update_brand_data)
                
                updated_brand_info = mapper.to(CarBrandResponse).map(updated_brands)
                
                response_serializer = BrandResponseSerializer(updated_brand_info)
                
                response = response_serializer.data
                
                EntityResponse = response
                apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
                return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            except IntegrityError:
                return Response({'error': 'Brand creation failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            print('entered Else')
            return Response(update_serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @staticmethod    
    def delete_async(ids: List[int]) -> bool:
        print('ids :', ids)
        try:
            deleted_count = BrandService.entity_service.delete_async(CarBrand, ids)
            if deleted_count > 0:
                return Response({'success': f'{deleted_count} brand(s) deleted successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'No brands were deleted.'}, status=status.HTTP_404_NOT_FOUND)

        except Http404:
            return Response({'error': 'brand not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Deletion failed. {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)