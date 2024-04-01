from django.db import models
from .BaseEntity.AuditableEntity import AuditableEntity

class User(AuditableEntity):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)