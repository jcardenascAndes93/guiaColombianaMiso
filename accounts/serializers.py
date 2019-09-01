from django.contrib.auth.models import User, Group
from .models import Profile
from rest_framework import serializers
from phone_field import PhoneField


class UserSerializer(serializers.HyperlinkedModelSerializer):
    first_name = serializers.CharField(
        source='profile.first_name', allow_blank=True, required=False)
    last_name = serializers.CharField(
        source='profile.last_name', allow_blank=True, required=False)
    phone = serializers.CharField(
        source='profile.phone', allow_blank=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username',  'password', 'email',
                  'first_name', 'last_name', 'phone')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        # user = super(UserSerializer, self).create(**validated_data)
        user = User.objects.create_user(**validated_data)
        self.update_or_create_profile(user, profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        self.update_or_create_profile(instance, profile_data)
        return super(UserSerializer, self).update(instance, validated_data)

    def update_or_create_profile(self, user, profile_data):
        # This always creates a Profile if the User is missing one;
        Profile.objects.update_or_create(user=user, defaults=profile_data)
