from django.db import models
from Core.BaseEntity.AuditableEntity import AuditableEntity

class CarModel(AuditableEntity):
    Model_name = models.CharField(max_length=100)
    Brand = models.ForeignKey('CarBrand', to_field='id', on_delete=models.CASCADE)