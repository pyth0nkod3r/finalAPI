from rest_framework import viewsets
#from .models import CategoryModel, OrderItemModel
from .models import MenuItemModel, CartModel, OrderModel, UserModel
from . import serializers


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