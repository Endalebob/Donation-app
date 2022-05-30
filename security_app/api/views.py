from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from security_app.api.serializers import *
from security_app import models

@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['GET',])
def get_all_user(request):
    if request.method == 'GET':
        USER = get_user_model()
        users = USER.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['POST',])
def registration(request):
    data = {}
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data['username'] = account.username
            data['email'] = account.email
            data['response'] = 'Successfully registered!'
            return Response(data)
        return Response(serializer.errors)


@api_view(['PUT', 'GET'])
def editprofile(request,username):
    user = get_object_or_404(User, username = username)
    data = {}
    if request.method == 'GET':
        serial = RegistrationSerializer(user)
        return Response(serial.data)

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data['username'] = account.username
            data['email'] = account.email
            data['response'] = 'Successfully registered!'
            return Response(data)
        return Response(serializer.errors)

