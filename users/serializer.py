from rest_framework import serializers
from users.models import User
from rest_framework.serializers import ValidationError


class SignupSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['email', 'name', 'dob', 'password','confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise ValidationError({"msg": "Passwords do not match"})
        return attrs

    def validate_email(self, email):
        email_exists = User.objects.filter(email=email)
        if email_exists:
            raise ValidationError({"msg": "Enter a unique email address"})
        return email

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data.get('email',None), email=validated_data.get('email',None), password=validated_data.get('password'), dob=validated_data.get('dob',None))
        return user


class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id','email','name','dob']
