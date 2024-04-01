from Infrastructure.Repository.Repository import Repository
from Core.Models.CarModel import CarModel
from Core.Models.CarBrand import CarBrand
from automapper import mapper
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from typing import List, Type
from django.db import IntegrityError
from Application.Interface.CarModelAbstractService import CarModelAbstractService
from Application.Dto.Model.CarModelRequest import CarModelRequest
from Application.Dto.Model.CarModelResponse import CarModelResponse
from WebAPI.Serializers.Model.CarModelRequestSeriliazer import CarModelRequestSerializer
from WebAPI.Serializers.Model.CarModelResponseSeriliazer import CarModelResponseSerializer
from WebAPI.Serializers.Brand.BrandResponseSeriliazer import BrandResponseSerializer
from Application.Dto.EntityResponse.EntityResponseModel import EntityResponseModel
from Application.Helpers.APIResponseHelper import APIResponseHelper


class ModelService(CarModelAbstractService):
    entity_service = Repository()
    
    @staticmethod
    def get_models(model_id=None):
        if model_id is not None:
            return ModelService.retrieve_model(model_id)
        else:
            return ModelService.list_models()
    
    @staticmethod
    def list_models():
        models = ModelService.entity_service.get_all_async(CarModel)
        
        serializer = CarModelResponseSerializer(models, many=True)
        models_data = serializer.data
        
        print('models_data', models_data)
        mapped_models = []
        
        for model_data in models_data:
            print('model_data', model_data)
            
            # brand = CarBrand.objects.get(id=model_data['Brand'])
            # brand_serializer = BrandResponseSerializer(brand)  # Remove many=True
            # brand_data = brand_serializer.data
            # print('brand', brand_data)
            
            # model_data['Brand'] = brand_data
            
            # brand = CarBrand.objects.get(id=model_data['Brand'])
            # model_data['Brand'] = brand
            
            # model = CarModel(**model_data)
            # print('model', model)
            
            mapped_model = mapper.to(CarModelResponse).map(model_data)
            
            mapped_models.append(vars(mapped_model))
        
        EntityResponse = mapped_models
        apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
        return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            
        # return Response(mapped_models, status=status.HTTP_200_OK)

    @staticmethod
    def retrieve_model(model_id):
        model = ModelService.entity_service.get_by_id_async(CarModel, model_id)
        
        if model is not None:
            model_info = mapper.to(CarModelResponse).map(model)
            
            serializer = CarModelResponseSerializer(model_info)
            response = serializer.data
            
            EntityResponse = response
            apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
            return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
        else:
            return Response({'error': 'Model not found.'}, status=status.HTTP_404_NOT_FOUND)
        
    @staticmethod
    def create_async(model: Type[CarModelRequest]) -> CarModel:
        serialized_data = CarModelRequestSerializer(data=model)
        
        if serialized_data.is_valid():
            model_data = serialized_data.validated_data
            print('model_data', model_data)
            
            model_data.pop('id', None)
            try:
                created_models = ModelService.entity_service.create_async(CarModel,**model_data)
                
                model_info = mapper.to(CarModelResponse).map(created_models)
                print('model_info', model_info)
                
                response_serializer = CarModelResponseSerializer(model_info)
                
                response = response_serializer.data
                
                EntityResponse = response
                print('EntityResponse', EntityResponse)
                apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
                return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            except IntegrityError:
                return Response({'error': 'Model creation failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            print('entered Else')
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @staticmethod   
    def update_async(updatemodel: Type[CarModelRequest]) -> CarModel:
        
        update_serialized_data = CarModelRequestSerializer( data=updatemodel)
        if update_serialized_data.is_valid():
            
            update_model_data = update_serialized_data.validated_data
            print('update_model_data', update_model_data)
            try:
                update_model_id = update_model_data['id']
                print('update_model_id', update_model_id)
                
                django_model = CarModel.objects.get(id=update_model_id)
                print('model: ', django_model.__dict__)
                
                if 'password' in update_model_data:
                    django_model.set_password(update_model_data['password'])
                django_model.save()
                
                print('django: ', django_model.__dict__)
                
                updated_models = ModelService.entity_service.update_async(CarModel, update_model_data)
                
                updated_model_info = mapper.to(CarModelResponse).map(updated_models)
                
                response_serializer = CarModelResponseSerializer(updated_model_info)
                
                response = response_serializer.data
                
                EntityResponse = response
                apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
                return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            except IntegrityError:
                return Response({'error': 'Model creation failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            print('entered Else')
            return Response(update_serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @staticmethod    
    def delete_async(ids: List[int]) -> bool:
        print('ids :', ids)
        try:
            deleted_count = ModelService.entity_service.delete_async(CarModel, ids)
            if deleted_count > 0:
                return Response({'success': f'{deleted_count} model(s) deleted successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'No models were deleted.'}, status=status.HTTP_404_NOT_FOUND)

        except Http404:
            return Response({'error': 'Model not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Deletion failed. {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
