from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models.base import ModelState
from .models import Product

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=126,min_length=6,write_only=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
    def validate(self, attrs):
        username = attrs.get('username',None)
        email = attrs.get('email',None)
        first_name = attrs.get('first_name',None)
        last_name = attrs.get('last_name',None)

        if not username:
            raise serializers.ValidationErro('Username is Required')
        if not first_name:
            raise serializers.ValidationError('First_name is required')

        if not email:
            raise serializers.ValidationError('Email id is required')

        if not last_name:
            raise serializers.ValidationError('Last_name is required')

        return attrs

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=126,)
    password = serializers.CharField(max_length=126,min_length=6,write_only=True)
    access_token = serializers.CharField(max_length=264,read_only=True)
    refresh_token = serializers.CharField(max_length=264,read_only=True)
    is_auth = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ['username','password','access_token','refresh_token','is_auth']

    def validate(self, attrs):
        username = attrs.get('username',None)
        password = attrs.get('password',None)
        
        user = authenticate(username=username,password=password)
        if not user:
            raise AuthenticationFailed("invalid credentials")
        if not user.is_active:
            raise AuthenticationFailed("user not activated")

        return {
            'username':user.username,
            'access_token':str(RefreshToken.for_user(user).access_token),
            'refresh_token':str(RefreshToken.for_user(user)),
            'is_auth':True
        }
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

