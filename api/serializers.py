# Serializers define the API representation.
from django.conf import settings
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



class PictureSerializer(serializers.ModelSerializer):
    """ Serializer for the :model:`pictures.models.Picture` """
    class Meta:
        model = Picture
        fields = ('id', 'url', 'student', 'picture')

    picture = serializers.SerializerMethodField('image_url')

    def image_url(self, picture):
        if picture.picture:
            return picture.picture.url
        elif picture.depth:
            return picture.depth.url
        else:
            return None


class PictureServerSerializer(serializers.ModelSerializer):
    """ Serializer for the :model:`pictures.models.Picture` for the android client “””
    class Meta:
        model = Picture
        fields = ('id', 'picture', 'depth')
