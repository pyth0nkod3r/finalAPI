from rest_framework import serializers
from .models import *
from django.contrib.auth.models import Group

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'slug']
        lookup_field = 'slug'
        
    
class MenuItemSerializer(CategorySerializer):
    category =  CategorySerializer(read_only=True)
    
    class Meta:
        model = MenuItemModel
        fields = ['id', 'title', 'featured', 'price', 'category',]
        read_only_fields = ('id',)
        
class CartSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()
    class Meta:
        model = CartModel
        fields = ['id', 'menu_item', 'user', 'quantity', 'unit_price', 'total_price']
        read_only_fields = ('id',)
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ['id', 'user', 'date', 'total_price', 'delivery_status', 'delivery_crew']
        read_only_fields = ('id')
        
class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    menu_item = MenuItemSerializer()
    class Meta:
        model = OrderItemModel
        fields = ['id', 'menu_item', 'order', 'quantity', 'unit_price', 'total_price']
        read_only_fields = ('id',)

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('__all__')