from .views import MenuItemView #, OrderView
#from .views import OrderItemView, SingleMenuItemView, CartView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('menu-items', MenuItemView, basename='menu-item')
urlpatterns = router.urls


# User Management
urlpatterns = [
    path('', include(router.urls)),
    path('users', include('djoser.urls')),
    path('users/me/', include('djoser.urls')),
    path('token/login/', include('djoser.urls')),
]

'''
# Order Management 
urlpatterns = [
    path('orders', OrderView.as_view()),
    path('orders/{orderId}', OrderItemView.as_view()),
]

# Cart Management
urlpatterns = [
    path('cart/menu-items', CartView.as_view()),
]

'''

