from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude =('user_permissions',)
        extra_kwargs = {
            'password':{'write_only':True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        img = validated_data.get('image', None)
        if img == 'image':
            user.img = img
            user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('is_staff', 'status_delete', 'is_active', 'is_superuser', 'password', 'user_permissions', 'groups')