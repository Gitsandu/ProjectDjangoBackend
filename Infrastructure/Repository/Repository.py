from typing import List, Type, TypeVar
from django.db import IntegrityError
from .AbstractRepository import AbstractRepository

TEntity = TypeVar('TEntity')

class Repository(AbstractRepository):
    @staticmethod
    def get_all_async(model: Type[TEntity]) -> List[TEntity]:
        return model.objects.all()

    @staticmethod
    def get_by_id_async(model: Type[TEntity], entity_id) -> TEntity:
        try:
            return model.objects.get(id=entity_id)
        except model.DoesNotExist:
            return None

    @staticmethod
    def get_by_name_async(model: Type[TEntity], entity_name) -> TEntity:
        try:
            return model.objects.get(username=entity_name)
        except model.DoesNotExist:
            return None
        
    @staticmethod
    def create_async(model: Type[TEntity], **kwargs) -> TEntity:
        try:
            entity = model.objects.create(**kwargs)
            return entity
        except IntegrityError as e:
            return None

    @staticmethod
    def update_async(model: Type[TEntity], update_data):
        entity_id = update_data['id']
        update_data.pop('id', None)
        updated_count = model.objects.filter(id=entity_id).update(**update_data)
        if updated_count > 0:
            response = model.objects.get(id=entity_id)
            return response
        else:
            return None
        
    @staticmethod
    def delete_async(model: Type[TEntity], entity_ids: List[int]) -> int:
        deleted_count, _ = model.objects.filter(id__in=entity_ids).delete()
        return deleted_count
    