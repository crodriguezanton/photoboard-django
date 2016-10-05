# Serializers define the API representation.
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


class PictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Picture
        fields = ('url', 'picture', 'student')