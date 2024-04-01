from rest_framework import serializers

class UserRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    is_deleted = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=False)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    phone_number = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    address = serializers.CharField(max_length=255)