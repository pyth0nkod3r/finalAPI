from django.shortcuts import render

# Create your views here.
from .models import UserModel
from rest_framework import generics
from .serializers import UserSerializer

class ManagerView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer 