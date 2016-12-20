from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import PictureRequestSerializer, ResponseSerializer
from upcauth.utils import checkLogin


class PictureRequestCreateView(CreateAPIView):
    serializer_class = PictureRequestSerializer


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
