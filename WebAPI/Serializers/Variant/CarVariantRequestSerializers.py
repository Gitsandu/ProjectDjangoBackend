from rest_framework import serializers
from  Core.Models.CarModel import CarModel

class CarVariantRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    is_deleted = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=False)
    Variant_Name = serializers.CharField(max_length=100)
    Model_Id = serializers.PrimaryKeyRelatedField(queryset=CarModel.objects.all())
    Fuel_Type = serializers.CharField(max_length=50)
    Launch_Year = serializers.IntegerField()
    Transmission = serializers.CharField(max_length =100, default = '')
