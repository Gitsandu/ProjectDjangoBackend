from Infrastructure.Repository.Repository import Repository
from Core.Models.CarVariant import CarVariant
from automapper import mapper
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from typing import List, Type
from django.db import IntegrityError
from Application.Interface.CarVariantAbstactService import CarVariantAbstractService
from Application.Dto.Variant.CarVariantRequest import CarVariantRequest
from Application.Dto.Variant.CarVariantResponse import CarVariantResponse
from WebAPI.Serializers.Variant.CarVariantRequestSerializers import CarVariantRequestSerializer
from WebAPI.Serializers.Variant.CarVariantResponseSerializers import CarVariantResponseSerializer
from Application.Dto.EntityResponse.EntityResponseModel import EntityResponseModel
from Application.Helpers.APIResponseHelper import APIResponseHelper

class VariantService(CarVariantAbstractService):
    entity_service = Repository()
    
    @staticmethod
    def get_variants(variant_id=None):
        if variant_id is not None:
            return VariantService.retrieve_variant(variant_id)
        else:
            return VariantService.list_variants()
    
    @staticmethod
    def list_variants():
        variants = VariantService.entity_service.get_all_async(CarVariant)
        
        serializer = CarVariantResponseSerializer(variants, many=True)
        variant_data = serializer.data
        
        mapped_variants = []
        
        for variant_data in variant_data:
            mapped_variant = mapper.to(CarVariantResponse).map(variant_data)
            mapped_variants.append(vars(mapped_variant))
        
        EntityResponse = mapped_variants
        apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
        return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
    
    @staticmethod
    def retrieve_variant(variant_id):
        variant = VariantService.entity_service.get_by_id_async(CarVariant, variant_id)
        
        if variant is not None:
            variant_info = mapper.to(CarVariantResponse).map(variant)
            serializer = CarVariantResponseSerializer(variant_info)
            response = serializer.data
            
            EntityResponse = response
            apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
            return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
        else:
            return Response({'error': 'Variant not found.'}, status=status.HTTP_404_NOT_FOUND)
        
    @staticmethod
    def create_async(variant: Type[CarVariantRequest]) -> CarVariant:
        print('tanish')

        serialized_data = CarVariantRequestSerializer(data=variant)
        print('serialized_data', serialized_data)

        if serialized_data.is_valid():
            variant_data = serialized_data.validated_data
            print('variant_data',variant_data)

            variant_data.pop('id', None)
            print('variant_data',variant_data)
            try:
                created_variant = VariantService.entity_service.create_async(CarVariant, **variant_data)
                print('created_variant : ',created_variant)

                variant_info = mapper.to(CarVariantResponse).map(created_variant)

                response_serializer = CarVariantResponseSerializer(variant_info)

                response = response_serializer.data

                EntityResponse = response

                apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
                return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            except IntegrityError:
                return Response({'error': 'Variant creation failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @staticmethod   
    def update_async(update_variant: Type[CarVariantRequest]) -> CarVariant:
        update_serialized_data = CarVariantRequestSerializer(data=update_variant)
        if update_serialized_data.is_valid():
            update_variant_data = update_serialized_data.validated_data
            
            try:
                update_variant_id = update_variant_data['id']
                django_variant = CarVariant.objects.get(id=update_variant_id)
                
                django_variant.save()
                updated_variant = VariantService.entity_service.update_async(CarVariant, update_variant_data)
                
                updated_variant_info = mapper.to(CarVariantResponse).map(updated_variant)
                response_serializer = CarVariantResponseSerializer(updated_variant_info)
                
                response = response_serializer.data
                
                EntityResponse = response
                apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
                return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            except IntegrityError:
                return Response({'error': 'Variant update failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(update_serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @staticmethod    
    def delete_async(ids: List[int]) -> bool:
        try:
            deleted_count = VariantService.entity_service.delete_async(CarVariant, ids)
            if deleted_count > 0:
                return Response({'success': f'{deleted_count} variant(s) deleted successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'No variants were deleted.'}, status=status.HTTP_404_NOT_FOUND)
        except Http404:
            return Response({'error': 'Variant not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Deletion failed. {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
