from rest_framework import serializers

class TokenPasswordSerlizer(serializers.Serializer):
    token = serializers.CharField(max_length=255)