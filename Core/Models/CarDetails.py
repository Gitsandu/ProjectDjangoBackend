from django.db import models
from Core.BaseEntity.AuditableEntity import AuditableEntity

class CarDetails(AuditableEntity):
    Location = models.CharField(max_length=100)
    Brand_Name = models.CharField(max_length=100)
    Model_Name = models.CharField(max_length=100)
    Variant_Name = models.CharField(max_length=100)
    MFD_Year = models.IntegerField()
    KiloMeter = models.CharField(max_length=100)
    Ownership = models.CharField(max_length=100)
    When_ToSell = models.CharField(max_length=100)
    User = models.ForeignKey('AuthUser', to_field='id', on_delete=models.CASCADE)
    FuelType = models.CharField(max_length =100)
    Transmission = models.CharField(max_length =100)