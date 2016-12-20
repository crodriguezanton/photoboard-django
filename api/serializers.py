# coding=utf-8
# Serializers define the API representation.
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import serializers

from education.models import Student, Subject
from pictures.models import Picture, PictureRequest, SubjectGallery


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the :model:django.contrib.auth.models.User """
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the :model:education.models.Student """
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


class PictureRequestSerializer(serializers.ModelSerializer):
    picture = PictureSerializer(read_only=True)

    class Meta:
        model = PictureRequest
        fields = ('url', 'uuid', 'ready', 'picture', 'subject')
        read_only_fields=('uuid', 'ready')


class ResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    error_code = serializers.IntegerField(required=False)
    error = serializers.CharField(max_length=200, required=False)


class SubjectSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Subject
        fields = ('id', 'code', 'name', 'short_name', 'subject_gallery')


class SubjectGallerySerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(read_only=True, many=True)
    subject = SubjectSerializer(read_only=True)
    class Meta:
        model = SubjectGallery
        fields = ('subject', 'pictures')