from django.urls import path

from .views import TeacherApiView, TeacherListApiView

app_name = "school"
urlpatterns = [
    path("listteachers/", TeacherListApiView.as_view()),
    path("teacher/", TeacherApiView.as_view()),
    path("teacher/?<uuid>", TeacherApiView.as_view()),
]
