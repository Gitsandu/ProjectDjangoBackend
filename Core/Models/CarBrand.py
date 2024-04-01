from django.db import models
from Core.BaseEntity.AuditableEntity import AuditableEntity

class CarBrand(AuditableEntity):
    Brandname = models.CharField(max_length=100)