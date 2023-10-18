from .views import MenuItemView #, OrderView
#from .views import OrderItemView, SingleMenuItemView, CartView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('menu-items', MenuItemView, basename='menu-item')
urlpatterns = router.urls


# Menu Items Management
urlpatterns = [
    path('', include(router.urls)),
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

