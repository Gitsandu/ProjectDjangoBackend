from django.db import models
from Core.BaseEntity.AuditableEntity import AuditableEntity

class Features(AuditableEntity):
    POWER_STEERING = models.BooleanField(default=False)
    POWER_WINDOWS_FRONT = models.BooleanField(default=False)
    AIR_CONDITIONER = models.BooleanField(default=False)
    HEATER = models.BooleanField(default=False)
    ADJUSTABLE_HEAD_LIGHTS = models.BooleanField(default=False)
    FOG_LIGHTS_FRONT = models.BooleanField(default=False)
    ANTI_LOCK_BRAKING_SYSTEM = models.BooleanField(default=False)
    CENTRAL_LOCKING = models.BooleanField(default=False)
    RADIO = models.BooleanField(default=False)
    Entertainment_communication = models.JSONField(default=dict)
    Safety = models.JSONField(default=dict)
    Exterior = models.JSONField(default=dict)
    Interior = models.JSONField(default=dict)
    Comfort_convenience = models.JSONField(default=dict)
    OverView = models.ForeignKey('CarOverview', to_field='id', on_delete=models.CASCADE) 
    