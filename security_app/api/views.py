from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from security_app.api.serializers import *
from rest_framework.decorators import api_view


@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST',])
def registration(request):
    data = {}
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data['username'] = account.username
            data['email'] = account.email
            data['token'] = Token.objects.get(user=account).key
            data['response'] = 'Successfully registered!'
            return Response(data)
        return Response(serializer.errors)

