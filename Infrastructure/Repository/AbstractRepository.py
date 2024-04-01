from typing import List, Type, TypeVar
from abc import ABC, abstractmethod
from django.db import IntegrityError

TEntity = TypeVar('TEntity')

class AbstractRepository(ABC):
    
    @abstractmethod
    def get_all_async(self, model: Type[TEntity]) -> List[TEntity]:
        pass

    @abstractmethod
    def get_by_id_async(self, model: Type[TEntity], entity_id) -> TEntity:
        pass

    @abstractmethod
    def get_by_name_async(self, model: Type[TEntity], entity_name) -> TEntity:
        pass

    @abstractmethod
    def create_async(self, model: Type[TEntity], **kwargs) -> TEntity:
        pass

    @abstractmethod
    def update_async(self, model: Type[TEntity], entity_id, update_data):
        pass

    @abstractmethod
    def delete_async(self, model: Type[TEntity], entity_ids: List[int]) -> int:
        pass