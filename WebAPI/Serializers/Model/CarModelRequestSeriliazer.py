from rest_framework import serializers
from Core.Models.CarBrand import CarBrand

class CarModelRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    is_deleted = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=False)
    Model_name = serializers.CharField(max_length=100)
    Brand = serializers.PrimaryKeyRelatedField(queryset=CarBrand.objects.all())
    
