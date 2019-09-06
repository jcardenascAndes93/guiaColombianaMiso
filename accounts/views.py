from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile
from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from .serializers import UserSerializer
from django.core import serializers
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# View of the API accounts endpoint MUST BE ADMIN USER!


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed, created or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_calsses = (AllowAny,)

    def post(self, request, *args, **kwargs):
        data = request.data

        user = authenticate(username=data.get('username'),
                            password=data.get('password'))

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'id': user.pk,
                             'fname': user.profile.first_name,
                             'lname': user.profile.last_name,
                             'email': user.email,
                             'phone': str(user.profile.phone)
                             }, status=200)

        return Response(status=400)
