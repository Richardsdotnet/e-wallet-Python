from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


from user.models import User
from user.serializers import UserSerializer


# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
