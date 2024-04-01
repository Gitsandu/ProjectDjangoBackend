from abc import ABC, abstractmethod
from typing import List, Type, TypeVar
from rest_framework.response import Response

TEntity = TypeVar('TEntity')

class CarVariantAbstractService(ABC):
    @abstractmethod
    def create_async(self, request: Type[TEntity]) -> TEntity:
        pass
    
    @abstractmethod
    def update_async(self, request: Type[TEntity]) -> TEntity:
        pass
    
    @abstractmethod
    def delete_async(self, ids: List[int]) -> bool:  
        pass
    
    @abstractmethod
    def list_variants(self) -> Response:
        pass
    
    @abstractmethod
    def retrieve_variant(self, variant_id: int) -> Response:
        pass
