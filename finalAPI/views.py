from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import *
from django.contrib.auth.models import User, Group
from .custom_permissions.permissions import IsManager

class SecretView(views.APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsManager]

    def get(self, request):
        return Response('Secret message', status=status.HTTP_200_OK)


class MenuItemView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsManager]
    queryset = MenuItemModel.objects.all()
    serializer_class = MenuItemSerializer

    def save(self, request, serializer):
        return serializer.save


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItemModel.objects.all()
    serializer_class = MenuItemSerializer


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
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def managers(self, request):
        username = request.data['username']
        if username:
            user = get_object_or_404(User, username=username)
            managers = Group.objects.get(name='Manager')
            if request.method == 'POST':
                managers.user_set.add(user)
                context = {'status': 'added'}
                return Response(context)
            elif request.method == 'GET':
                return managers
            elif request.method == 'DELETE':
                managers.user_set.remove(user)
                context = {'status': 'removed'}
                return Response(context)
        context = {"status": "error"}
        return Response(context, status.HTTP_400_BAD_REQUEST)
