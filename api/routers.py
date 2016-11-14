from rest_framework import routers

from api.viewsets import UserViewSet, PictureViewSet, StudentViewSet

"""Defining urls for API"""
default_router = routers.DefaultRouter()
default_router.register(r'users', UserViewSet)
default_router.register(r'students', StudentViewSet)
default_router.register(r'pictures', PictureViewSet)
