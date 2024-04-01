from rest_framework import serializers

class LocationRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    city_name = serializers.CharField(max_length=20)
    pin_code = serializers.CharField(max_length=6)
    state = serializers.CharField(max_length=20)