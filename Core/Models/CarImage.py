from django.db import models
from cloudinary.models import CloudinaryField
from Core.BaseEntity.AuditableEntity import AuditableEntity

class CarImage(AuditableEntity):
  Image = CloudinaryField('image')
  OverView = models.ForeignKey('CarOverview', to_field='id', on_delete=models.CASCADE)
  