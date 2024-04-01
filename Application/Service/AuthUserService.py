from Infrastructure.Repository.Repository import Repository
from Core.Models.AuthUser import AuthUser
from automapper import mapper
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from typing import List, Type
from django.db import IntegrityError
from Application.Interface.AuthUserAbstractService import AuthUserAbstractService
from Application.Dto.AuthUser.AuthUserRequest import AuthUserRequest
from Application.Dto.AuthUser.AuthUserResponse import AuthUserResponse
from WebAPI.Serializers.AuthUser.AuthUserRequestSerializer import AuthUserRequestSerializer
from WebAPI.Serializers.AuthUser.AuthUserResponseSerializer import AuthUserResponseSerializer
from Application.Dto.EntityResponse.EntityResponseModel import EntityResponseModel
from Application.Helpers.APIResponseHelper import APIResponseHelper
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

class AuthUserService(AuthUserAbstractService):
    entity_service = Repository()
    
    @staticmethod
    def get_users(user_id=None):
        if user_id is not None:
            return AuthUserService.retrieve_user(user_id)
        else:
            return AuthUserService.list_users()
                
    @staticmethod
    def list_users():
        users = AuthUserService.entity_service.get_all_async(AuthUser)
        
        serializer = AuthUserResponseSerializer(users, many=True)
        users_data = serializer.data
        
        mapped_users = []
        
        for user_data in users_data:
            user = AuthUser(**user_data)
            
            mapped_user = mapper.to(AuthUserResponse).map(user)
            
            mapped_users.append(vars(mapped_user))
        
        EntityResponse = mapped_users
        apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
        return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            
        # return Response(mapped_users, status=status.HTTP_200_OK)

    @staticmethod
    def retrieve_user(user_id):
        user = AuthUserService.entity_service.get_by_id_async(AuthUser, user_id)
        
        if user is not None:
            user_info = mapper.to(AuthUserResponse).map(user)
            
            serializer = AuthUserResponseSerializer(user_info)
            response = serializer.data
            
            EntityResponse = response
            apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
            return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
        else:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        
    @staticmethod
    def retrieve_user_name(user_name):
        user = AuthUserService.entity_service.get_by_name_async(AuthUser, user_name)
        
        if user is not None:
            user_info = mapper.to(AuthUserResponse).map(user)
            
            serializer = AuthUserResponseSerializer(user_info)
            response = serializer.data
        return response
        
        
    @staticmethod
    def create_async(model: Type[AuthUserRequest]) -> AuthUser:
        serialized_data = AuthUserRequestSerializer(data=model)
        print('serialized_data', serialized_data)
        
        if serialized_data.is_valid():
            user_data = serialized_data.validated_data
            print('user_data', user_data)
            user_data.pop('id', None)
            
            try:
                django_user = User.objects.create_user(username=user_data['username'], password=user_data['password'])
                print('django_user', django_user)
                
                hashedPass = user_data['password']
                print('hashedPass', hashedPass)

                hashed_password = make_password(user_data['password'])
                print('hashed_password', hashed_password)
                
                user_data['password'] = hashed_password
               
                created_users = AuthUserService.entity_service.create_async(AuthUser,**user_data)
               
                user_info = mapper.to(AuthUserResponse).map(created_users)
               
                response_serializer = AuthUserResponseSerializer(user_info)
               
                response = response_serializer.data
               
                checkPass = response['password']
                print('checkPass', checkPass)
 
                if(check_password(hashedPass, checkPass)):
                    print('password checked')
                else:
                    print('password check failed')
                    
                EntityResponse = response
                print('EntityResponse', EntityResponse)
                apiResponse = APIResponseHelper.get_instance().convert_to_api_response(EntityResponse)
                return EntityResponseModel(EntityResponse=EntityResponse, APIResponse=apiResponse)
            except IntegrityError:
                return Response({'error': 'User creation failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            print('entered Else')
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    @staticmethod   
    def update_async(updatemodel: Type[AuthUserRequest]) -> AuthUser:
        
        update_serialized_data = AuthUserRequestSerializer( data=updatemodel)
        if update_serialized_data.is_valid():
            
            update_user_data = update_serialized_data.validated_data
            print('update_user_data', update_user_data)
            try:
                update_user_id = update_user_data['id']
                print('update_user_id', update_user_id)
                
                django_user = User.objects.get(id=update_user_id)
                print('user: ', django_user.__dict__)
                
                if 'password' in update_user_data:
                    django_user.set_password(update_user_data['password'])
                django_user.save()
                
                print('django: ', django_user.__dict__)
                
                updated_users = AuthUserService.entity_service.update_async(AuthUser, update_user_data)
                
                updated_user_info = mapper.to(AuthUserResponse).map(updated_users)
                
                response_serializer = AuthUserResponseSerializer(updated_user_info)
                
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
            deleted_count = AuthUserService.entity_service.delete_async(AuthUser, ids)
            if deleted_count > 0:
                return Response({'success': f'{deleted_count} user(s) deleted successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'No users were deleted.'}, status=status.HTTP_404_NOT_FOUND)

        except Http404:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Deletion failed. {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)