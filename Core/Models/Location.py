from django.db import models
from Core.BaseEntity.AuditableEntity import AuditableEntity

class Location(AuditableEntity):
    city_name = models.CharField(max_length=20)
    pin_code = models.CharField(max_length=6)
    state = models.CharField(max_length=20)