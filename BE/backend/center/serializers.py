from rest_framework import serializers

from .models import Center, CenterUser

class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = ['id', 'name', 'address', 'homepage', 'telephone']

class CenterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterUser
        fields = "__all__"