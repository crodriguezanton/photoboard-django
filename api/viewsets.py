# ViewSets define the view behavior.
from django.contrib.auth.models import User
from rest_framework import viewsets

from api.serializers import UserSerializer, PictureSerializer, StudentSerializer
from pictures.models import Picture
from education.models import Student


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
