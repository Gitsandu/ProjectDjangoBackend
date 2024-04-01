from rest_framework import serializers
from  Core.Models.AuthUser import AuthUser

class CarOverViewResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    is_deleted = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=False)
    created_by = serializers.UUIDField(read_only=True)
    updated_by = serializers.UUIDField(read_only=True)
    created_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)
    Location = serializers.CharField(max_length=100)
    Brand_Name = serializers.CharField(max_length=100)
    Model_Name = serializers.CharField(max_length=100)
    Variant_Name = serializers.CharField(max_length=100)
    MFD_Year = serializers.IntegerField()
    KiloMeter = serializers.CharField(max_length=100)
    Ownership = serializers.CharField(max_length=100)
    When_ToSell = serializers.CharField(max_length=100)
    User = serializers.PrimaryKeyRelatedField(queryset=AuthUser.objects.all())
    Price = serializers.CharField(max_length = 100)
    Insurance = serializers.CharField(max_length = 100)
    EngineCapacity = serializers.CharField(max_length =100)
    FuelType = serializers.CharField(max_length =100)
    Transmission = serializers.CharField(max_length =100)
    Seats = serializers.IntegerField()
    Image = serializers.CharField(max_length=100, default = '')
    

