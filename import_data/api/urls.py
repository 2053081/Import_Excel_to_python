from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path("file_upload", csrf_exempt(views.file_upload), name="file_upload"),
]
