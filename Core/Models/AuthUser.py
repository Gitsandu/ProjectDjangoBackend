from django.db import models
from Core.BaseEntity.AuditableEntity import AuditableEntity

class AuthUser(AuditableEntity):
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)