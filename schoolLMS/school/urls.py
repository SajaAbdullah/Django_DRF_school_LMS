from django.urls import path

from .views import ListTeacherView, SingleTeacherView

urlpatterns = [
    path("teacher/", SingleTeacherView.as_view()),
    path("teacher/<uuid:uuid>/", SingleTeacherView.as_view()),  # url parms
    path("teacher/?<uuid>", SingleTeacherView.as_view()),  # quary parms
    path("teachersList/", ListTeacherView.as_view()),
]
