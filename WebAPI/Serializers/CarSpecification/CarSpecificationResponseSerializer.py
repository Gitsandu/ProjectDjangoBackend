from rest_framework import serializers
from  Core.Models.CarOverview import CarOverview

class CarSpecificationResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField(default=False, read_only=True)
    is_active = serializers.BooleanField(default=False)
    created_by = serializers.UUIDField(read_only=True)
    updated_by = serializers.UUIDField(read_only=True)
    created_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)
    mileage = serializers.CharField(max_length=100)
    engine = serializers.CharField(max_length=100)
    max_power = serializers.CharField(max_length=100)
    torque = serializers.CharField(max_length=100)
    seats = serializers.CharField(max_length=100)
    wheel = serializers.CharField(max_length=100)
    engine_and_transmission = serializers.JSONField(default=dict)
    dimensions_and_capacity = serializers.JSONField(default=dict)
    miscellaneous = serializers.JSONField(default=dict)
    OverView = serializers.PrimaryKeyRelatedField(queryset=CarOverview.objects.all())
    
    
