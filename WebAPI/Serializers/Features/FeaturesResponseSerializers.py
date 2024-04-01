from rest_framework import serializers
from  Core.Models.CarOverview import CarOverview

class FeaturesResponseSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField(default=False, read_only=True)
    is_active = serializers.BooleanField(default=False)
    created_by = serializers.UUIDField(read_only=True)
    updated_by = serializers.UUIDField(read_only=True)
    created_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)
    POWER_STEERING = serializers.BooleanField(default=False)
    POWER_WINDOWS_FRONT = serializers.BooleanField(default=False)
    AIR_CONDITIONER = serializers.BooleanField(default=False)
    HEATER = serializers.BooleanField(default=False)
    ADJUSTABLE_HEAD_LIGHTS = serializers.BooleanField(default=False)
    FOG_LIGHTS_FRONT = serializers.BooleanField(default=False)
    ANTI_LOCK_BRAKING_SYSTEM = serializers.BooleanField(default=False)
    CENTRAL_LOCKING = serializers.BooleanField(default=False)
    RADIO = serializers.BooleanField(default=False)
    Entertainment_communication = serializers.JSONField(default=dict)
    Safety = serializers.JSONField(default=dict)
    Exterior = serializers.JSONField(default=dict)
    Interior = serializers.JSONField(default=dict)
    Comfort_convenience = serializers.JSONField(default=dict)
    OverView = serializers.PrimaryKeyRelatedField(queryset=CarOverview.objects.all())
    