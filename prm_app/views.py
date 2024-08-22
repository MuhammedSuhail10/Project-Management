from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
from .serializers import *

# Login
class LoginView(APIView):
    def post(self,request):
        data=request.data
        username = data.get('phone')
        password = data.get('password')
        user =  authenticate(username=username,password=password)
        if user is not None:
            user = User.objects.get(username=username)
            user.last_login = timezone.now()
            user.save()
            resp = {'status':True,'userid':user.id}
        else:
            resp = {'status':False,'message': 'Incorrect username or password'}
        return Response(resp)

class Users(APIView):
    def post(self,request):
        if User.objects.filter(username=data.get('username')).exists():
            return Response({'status':False,'message':'User already exists'})
        serializer = UserSerial(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':True})
        else:
            return Response(serializer.errors)