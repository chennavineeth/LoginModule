from django.contrib.auth import get_user_model
from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(min_length=8,write_only=True,max_length=30)
    class Meta:
        model = get_user_model()
        fields = ['username','password','first_name', 'last_name']

    def validate(self,args):
        username=args.get('username',None)
        if get_user_model().objects.filter(username=username).exists():
            raise serializers.ValidationError({"username":("username already exist ")})

        return super().validate(args)

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields='__all__'
    


# User serializer