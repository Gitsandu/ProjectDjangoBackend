from django.db import models
from Core.BaseEntity.AuditableEntity import AuditableEntity

class CarVariant(AuditableEntity):
    Variant_Name = models.CharField(max_length=100)
    Model_Id = models.ForeignKey('CarModel', to_field='id', on_delete=models.CASCADE)
    Fuel_Type = models.CharField(max_length=50)
    Launch_Year = models.IntegerField()
    Transmission = models.CharField(max_length =100, default='')

    
