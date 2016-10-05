from rest_framework import routers

from api.viewsets import UserViewSet

default_router = routers.DefaultRouter()
default_router.register(r'users', UserViewSet)
