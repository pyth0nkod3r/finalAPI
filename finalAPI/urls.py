from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('menu-items', MenuItemView, basename='menu-item'),
#router.register('secret', SecretView, basename='secretview')



# User Management
urlpatterns = [
    path('secret', SecretView.as_view()),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]

urlpatterns += router.urls