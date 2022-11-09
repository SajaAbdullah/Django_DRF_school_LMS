from django.urls import path

from .views import (
    TeacherCreateGenaricView,
    TeacherListGenaricView,
    TeacherRetrieveGenaricView,
)

app_name = "school"
urlpatterns = [
    path("list_teachers/", TeacherListGenaricView.as_view(), name="teachers_list_api"),
    path(
        "retrieve_teacher/<uuid:id>",
        TeacherRetrieveGenaricView.as_view(),
        name="retrieve_teacher",
    ),
    path("create/", TeacherCreateGenaricView.as_view(), name="create_teacher"),
]
