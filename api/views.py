from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import PictureRequestSerializer, ResponseSerializer, SubjectSerializer
from education.models import Subject
from pictures.models import PictureRequest, Picture, SubjectGallery
from upcauth.utils import checkLogin, getCourses
from pictures.utils import call_socket


class PictureRequestCreateView(CreateAPIView):
    serializer_class = PictureRequestSerializer


class PictureRequestView(APIView):
    def post(self, request, format=None):
        pr = PictureRequest.objects.create(subject=Subject.objects.get(pk=request.data.get("subject", None)))

        call_socket(str(pr.uuid))

        serializer = PictureRequestSerializer(pr, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class UPCLoginView(APIView):
    def post(self, request, format=None):
        loggedin = checkLogin(request.data.get("email", ""), request.data.get("password", ""))

        data = {
            'success': loggedin,
            'error_code': 0,
            'error': "None",
        }

        serializer = ResponseSerializer(data=data)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetSubjectsView(APIView):
    def post(self, request, format=None):
        subjects = getCourses(request.data.get("email", ""), request.data.get("password", ""))

        serializer = SubjectSerializer(subjects, many=True, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class UploadPictureView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, uuid, format=None):
        picture = request.FILES.get('picture')
        depth = request.FILES.get('depth')

        pr = PictureRequest.objects.get(pk=uuid)
        pr.picture = Picture.objects.create(
            picture = picture,
            depth = depth,
            gallery = SubjectGallery.objects.get(subject=pr.subject)
        )
        pr.ready = True
        pr.save()

        serializer = PictureRequestSerializer(pr, context={'request': request})

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
