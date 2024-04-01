from rest_framework import serializers

class BrandRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    is_deleted = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=False)
    Brandname = serializers.CharField(max_length=100)