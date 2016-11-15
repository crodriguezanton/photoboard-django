# Serializers define the API representation.
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import serializers

from education.models import Student
from pictures.models import Picture


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url', 'user')


class PictureSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Picture
        fields = ('id', 'picture', 'depth')