from rest_framework import serializers
from  Core.Models.CarBrand import CarBrand

class CarModelResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField(default=False, read_only=True)
    is_active = serializers.BooleanField(default=False)
    Model_name = serializers.CharField(max_length=100)
    Brand = serializers.PrimaryKeyRelatedField(queryset=CarBrand.objects.all())
    created_by = serializers.UUIDField(read_only=True)
    updated_by = serializers.UUIDField(read_only=True)
    created_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)
