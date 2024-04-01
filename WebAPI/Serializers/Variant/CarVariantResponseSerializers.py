from rest_framework import serializers
from  Core.Models.CarModel import CarModel

class CarVariantResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField(default=False, read_only=True)
    is_active = serializers.BooleanField(default=False)
    Model_Id = serializers.PrimaryKeyRelatedField(queryset=CarModel.objects.all())
    Variant_Name = serializers.CharField(max_length=100)
    Fuel_Type = serializers.CharField(max_length=50)
    Launch_Year = serializers.IntegerField()
    created_by = serializers.UUIDField(read_only=True)
    updated_by = serializers.UUIDField(read_only=True)
    created_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)
    Transmission = serializers.CharField(max_length =100, default = '')
