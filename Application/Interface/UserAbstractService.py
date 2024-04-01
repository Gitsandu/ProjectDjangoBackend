from abc import ABC, abstractmethod
from typing import List, Type, TypeVar
from rest_framework.response import Response

TEntity = TypeVar('TEntity')

class UserAbstractService(ABC):
    @abstractmethod
    def create_async(self, request: Type[TEntity],) -> TEntity:
        pass
    
    @abstractmethod
    def update_async(self, request: Type[TEntity],) -> TEntity:
        pass
    
    @abstractmethod
    def delete_async(self, ids: List[int]) -> bool:  
        pass
    
    @abstractmethod
    def list_users(self) -> Response:
        pass
    
    @abstractmethod
    def retrieve_user(self, user_id) -> Response:
        pass
    