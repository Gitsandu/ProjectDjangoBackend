from rest_framework import serializers
from  Core.Models.AuthUser import AuthUser

class CarDetialsResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField(default=False, read_only=True)
    is_active = serializers.BooleanField(default=False)
    Location = serializers.CharField(max_length=100)
    Brand_Name = serializers.CharField(max_length=100)
    Model_Name = serializers.CharField(max_length=100)
    Variant_Name = serializers.CharField(max_length=100)
    MFD_Year = serializers.IntegerField()
    KiloMeter = serializers.CharField(max_length=100)
    Ownership = serializers.CharField(max_length=100)
    When_ToSell = serializers.CharField(max_length=100)
    created_by = serializers.UUIDField(read_only=True)
    updated_by = serializers.UUIDField(read_only=True)
    created_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)
    User = serializers.PrimaryKeyRelatedField(queryset=AuthUser.objects.all())
    FuelType = serializers.CharField(max_length =100)
    Transmission = serializers.CharField(max_length =100)

