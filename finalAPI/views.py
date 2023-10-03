from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from .models import *
from . import serializers
#from rest_framework.authtoken.views import obtain_auth_token

class SecretView(APIView):
    def get(self, request):
        return Response('Secret message', status=status.HTTP_200_OK)

class MenuItemView(viewsets.ModelViewSet):
    queryset = MenuItemModel.objects.all()
    serializer_class = serializers.MenuItemSerializer
    
    def save(self, serializer):
       serializer.save()
       

'''
class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItemModel.objects.all()
    serializer_class = serializers.MenuItemSerializer


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