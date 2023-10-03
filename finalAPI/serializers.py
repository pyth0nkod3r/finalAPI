from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'slug']
        lookup_field = 'slug'
    
class MenuItemSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    #category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = MenuItemModel
        fields = ['id', 'title', 'featured', 'price', 'category',]
    
class CartSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()
    class Meta:
        model = CartModel
        fields = ['id', 'menu_item', 'user', 'quantity', 'unit_price', 'total_price']
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ['id', 'user', 'date', 'total_price', 'delivery_status', 'delivery_crew']
        
class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    menu_item = MenuItemSerializer()
    class Meta:
        model = OrderItemModel
        fields = ['id', 'menu_item', 'order', 'quantity', 'unit_price', 'total_price']