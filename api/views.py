from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from api.serializers import PictureRequestSerializer


class PictureRequestCreateView(CreateAPIView):
    serializer_class = PictureRequestSerializer