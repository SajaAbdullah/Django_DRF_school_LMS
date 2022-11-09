from django.urls import path

from .views import (
    TeacherCreateGenaricView,
    TeacherDeleteGenaricView,
    TeacherListGenaricView,
    TeacherRetrieveGenaricView,
    TeacherUpdateGenaricView,
)

app_name = "school"
urlpatterns = [
    path("list_teachers/", TeacherListGenaricView.as_view(), name="teachers_list_api"),
    path(
        "retrieve_teacher/<uuid:id>",
        TeacherRetrieveGenaricView.as_view(),
        name="retrieve_teacher",
    ),
    path("create_teacher/", TeacherCreateGenaricView.as_view(), name="create_teacher"),
    path(
        "update_teacher/<uuid:id>",
        TeacherUpdateGenaricView.as_view(),
        name="update_teacher",
    ),
    path(
        "delete_teacher/<uuid:id>",
        TeacherDeleteGenaricView.as_view(),
        name="delete_teacher",
    ),
]
