from urllib import request
from django.shortcuts import render,redirect
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import RegisterSerializer ,UserSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny 
from rest_framework.permissions import IsAuthenticated
from rest_framework import  serializers 
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegisterApiView(generics.GenericAPIView):
    permission_classes=[AllowAny,]
    serializer_class=RegisterSerializer
    print("views")
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return redirect('token')
        else:
            return Response({"status":"inavalid detais"})


class LoginAPIView(APIView):
    def get_data(self,request,username):
        p=get_user_model().objects.get(username=username)
        ans=p.last_name
        print("hello",ans)
        return ans

class DetailsAPIView(LoginAPIView ):
    #authentication_classes=[JWTAuthentication,]
    #permission_classes=[IsAuthenticated,]
    def get(self,request, format=None):
        p=request.user.username
        a=super().get_data(request,p)
        print("last_name",a)
        # if request.user.is_authenticated == True:
        #     return Response("Valid Credentials", status=200)
        return Response({"status":"you are verified user ","name":a})

    def post(self,request,format=None):
        
        print("Login Class")

        user_obj = get_user_model().objects.get(username=request.user)

        if user_obj is not None:
            credentials = {
                'username': user_obj.username,
                'password': request.data['password']
            }
            user = authenticate(**credentials)

            if user and user.is_active:
                # user_serializer = (user)
                return Response("Logged in", status=200)

        return Response("Invalid Credentials", status=403)

    

    


# Create your views here.
