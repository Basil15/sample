from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'bio', 'profile_picture']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'bio', 'profile_picture']
        read_only_fields = ['id']
        extra_kwargs = {
            'email': {'validators': []},  # disable default email validation
        }

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required.")
        return value

    def validate(self, data):
        email = data.get('email')
        if email and UserProfile.objects.filter(email=email).exclude(user=self.context['request'].user).exists():
            raise serializers.ValidationError("Email already exists.")
        return data
