from rest_framework import serializers

class UserResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField(default=False, read_only=True)
    is_active = serializers.BooleanField(default=False)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    phone_number = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    address = serializers.CharField(max_length=255)
    created_by = serializers.UUIDField(read_only=True)
    updated_by = serializers.UUIDField(read_only=True)
    created_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)
