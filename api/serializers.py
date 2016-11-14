p# Serializers define the API representation.
from django.contrib.auth.models import User
from rest_framework import serializers

from education.models import Student
from pictures.models import Picture


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the :model:`django.contrib.auth.models.User` """
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the :model:`education.models.Student` """
    class Meta:
        model = Student
        fields = ('url', 'user')


class PictureSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the :model:`pictures.models.Picture` """
    class Meta:
        model = Picture
        fields = ('url', 'picture', 'student')
