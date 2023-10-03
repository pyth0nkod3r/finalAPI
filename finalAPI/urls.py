from .views import *
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

'''
router = DefaultRouter(trailing_slash=False)
router.register('menu-items', MenuItemView, basename='menu-item'),
#router.register('menu-items/<int:pk>', SingleMenuItemView, basename='single-item'),

'''


# User Management
urlpatterns = [
    path('secret', SecretView.as_view()),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    re_path('menu-items/?$', MenuItemView.as_view()),
    re_path('menu-items/<int:pk>/?$', SingleMenuItemView.as_view(),)
]

#urlpatterns += router.urls