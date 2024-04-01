from django.db import models
from Core.BaseEntity.AuditableEntity import AuditableEntity

class CarSpecification(AuditableEntity):
    mileage = models.CharField(max_length=50)
    engine = models.CharField(max_length=50)
    max_power = models.CharField(max_length=50)
    torque = models.CharField(max_length=50)
    seats = models.PositiveSmallIntegerField()
    wheel = models.CharField(max_length=50)
    engine_and_transmission = models.JSONField(default=dict)
    dimensions_and_capacity = models.JSONField(default=dict)
    miscellaneous = models.JSONField(default=dict)
    OverView = models.ForeignKey('CarOverview', to_field='id', on_delete=models.CASCADE) 
