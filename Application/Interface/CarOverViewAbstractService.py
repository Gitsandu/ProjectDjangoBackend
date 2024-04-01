from abc import ABC, abstractmethod
from typing import List, Type, TypeVar
from rest_framework.response import Response

TEntity = TypeVar('TEntity')

class CarOverViewAbstractService(ABC):    
    @abstractmethod
    def list_details(self) -> Response:
        pass
    
    @abstractmethod
    def retrieve_detail(self, cardetail_id) -> Response:
        pass
    