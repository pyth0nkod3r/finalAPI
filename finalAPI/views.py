from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from . import serializers
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import *
from django.contrib.auth.models import User, Group


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

class ManagerView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

    def managers(self, request):
        username = request.data['username']
        if username:
            user = get_object_or_404(User, username=username)
            managers = Group.objects.get(name='Manager')
            managers.user_set.add(user)
            context = {'status': 'added'}
            return Response(context)
        context = {"status": "error"}
        return Response(context, status.HTTP_400_BAD_REQUEST)