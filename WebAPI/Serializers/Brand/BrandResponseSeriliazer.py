from rest_framework import serializers

class BrandResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField(default=False, read_only=True)
    is_active = serializers.BooleanField(default=False)
    Brandname = serializers.CharField(max_length=100)
    created_by = serializers.UUIDField(read_only=True)
    updated_by = serializers.UUIDField(read_only=True)
    created_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)
