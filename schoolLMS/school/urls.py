from django.urls import path

from .views import TeacherListApiView

urlpatterns = [
    path("listteachers/", TeacherListApiView.as_view()),
]
