from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from . import serializers
from django.shortcuts import get_object_or_404
from rest_framework.generics import *


class SecretView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response('Secret message', status=status.HTTP_200_OK)

class MenuItemView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = MenuItemModel.objects.all()
    serializer_class = serializers.MenuItemSerializer
    
    def save(self, serializer):
       serializer.save()
       


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItemModel.objects.all()
    serializer_class = serializers.MenuItemSerializer
    
'''

class CartView(ListCreateAPIView):
    queryset = CartModel.objects.all()
    serializer_class = serializers.CartSerializer


class OrderView(ListCreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderItemView(RetrieveUpdateAPIView):
    queryset = OrderItemModel.objects.all()
    serializer_class = serializers.OrderItemSerializer

'''