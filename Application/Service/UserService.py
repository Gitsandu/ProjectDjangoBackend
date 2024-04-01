from Infrastructure.Repository.Repository import Repository
from Core.User import User
from automapper import mapper
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from typing import List, Type
from django.db import IntegrityError
from Application.Interface.UserAbstractService import UserAbstractService
from Application.Dto.User.UserRequest import UserRequest
from Application.Dto.User.UserResponse import UserResponse
from WebAPI.Serializers.User.UserRequestSerializer import UserRequestSerializer
from WebAPI.Serializers.User.UserResponseSerializer import UserResponseSerializer
from Application.Dto.EntityResponse.EntityResponseModel import EntityResponseModel
from Application.Helpers.APIResponseHelper import APIResponseHelper

class UserService(UserAbstractService):
    entity_service = Repository()
    
    @staticmethod
    def get_users(user_id=None):
        if user_id is not None:
            return UserService.retrieve_user(user_id)
        else:
            return UserService.list_users()
    
    @staticmethod
    def list_users():
        users = UserService.entity_service.get_all_async(User)
        
        serializer = UserResponseSerializer(users, many=True)
        users_data = serializer.data
        
        mapped_users = []
        
        for user_data in users_data:
            user = User(**user_data)
            
            mapped_user = mapper.to(UserResponse).map(user)
            
            mapped_users.append(vars(mapped_user))
        
        EntityResponse = mapped_users
        apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
        return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            
        # return Response(mapped_users, status=status.HTTP_200_OK)

    @staticmethod
    def retrieve_user(user_id):
        user = UserService.entity_service.get_by_id_async(User, user_id)
        
        if user is not None:
            user_info = mapper.to(UserResponse).map(user)
            
            serializer = UserResponseSerializer(user_info)
            response = serializer.data
            
            EntityResponse = response
            apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
            return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
        else:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        
    @staticmethod
    def create_async(model: Type[UserRequest]) -> User:
        serialized_data = UserRequestSerializer(data=model)
        
        if serialized_data.is_valid():
            user_data = serialized_data.validated_data
            user_data.pop('id', None)
            try:
                
                created_users = UserService.entity_service.create_async(User,**user_data)
                
                user_info = mapper.to(UserResponse).map(created_users)
                
                response_serializer = UserResponseSerializer(user_info)
                
                response = response_serializer.data
                
                EntityResponse = response
                apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
                return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            except IntegrityError:
                return Response({'error': 'User creation failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            print('entered Else')
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @staticmethod   
    def update_async(updatemodel: Type[UserRequest]) -> User:
        
        update_serialized_data = UserRequestSerializer( data=updatemodel)
        if update_serialized_data.is_valid():
            
            update_user_data = update_serialized_data.validated_data
            try:
                updated_users = UserService.entity_service.update_async(User, update_user_data)

                updated_user_info = mapper.to(UserResponse).map(updated_users)
                
                response_serializer = UserResponseSerializer(updated_user_info)
                
                response = response_serializer.data
                
                EntityResponse = response
                apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
                return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            except IntegrityError:
                return Response({'error': 'User creation failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            print('entered Else')
            return Response(update_serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @staticmethod    
    def delete_async(ids: List[int]) -> bool:
        print('ids :', ids)
        try:
            deleted_count = UserService.entity_service.delete_async(User, ids)
            if deleted_count > 0:
                return Response({'success': f'{deleted_count} user(s) deleted successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'No users were deleted.'}, status=status.HTTP_404_NOT_FOUND)

        except Http404:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Deletion failed. {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)