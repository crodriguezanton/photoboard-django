"""photoboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from api.routers import default_router
from api.views import PictureRequestCreateView, UPCLoginView, GetSubjectsView, PictureRequestView, UploadPictureView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(default_router.urls)),
    url(r'^api/create-request', PictureRequestCreateView.as_view()),
    url(r'^api/login', UPCLoginView.as_view()),
    url(r'^api/subjects', GetSubjectsView.as_view()),
    url(r'^api/picture-request', PictureRequestView.as_view()),
    url(r'^api/upload-picture/(?P<uuid>[^/]+)', UploadPictureView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
