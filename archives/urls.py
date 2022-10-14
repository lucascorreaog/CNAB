from django.urls import path

from . import views

urlpatterns = [
    path("archive/", views.UpFile.as_view()),
    path("archive/info_list", views.ArchiveView.as_view()),
]