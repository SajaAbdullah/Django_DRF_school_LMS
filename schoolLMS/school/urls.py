from django.urls import path

from .views import (
    TeacherClassCreateView,
    TeacherClassListView,
    TeacherCreateView,
    TeacherListView,
    TeacherRUDView,
    TeahcerExpertyListView,
)

app_name = "school"
urlpatterns = [
    path("list_teacher/", TeacherListView.as_view(), name="list_teacher"),
    path(
        "retrieve_teacher/<uuid:id>",
        TeacherRUDView.as_view(),
        name="retrieve_teacher",
    ),
    path("create_teacher/", TeacherCreateView.as_view(), name="create_teacher"),
    path(
        "update_teacher/<uuid:id>",
        TeacherRUDView.as_view(),
        name="update_teacher",
    ),
    path(
        "delete_teacher/<uuid:id>",
        TeacherRUDView.as_view(),
        name="delete_teacher",
    ),
    path(
        "create_teacher_class/",
        TeacherClassCreateView.as_view(),
        name="create_teacher_class",
    ),
    path(
        "list_teacher_classes/<uuid:teacher>",
        TeacherClassListView.as_view(),
        name="list_teacher_classes",
    ),
    path(
        "list_teacher_experty/<uuid:teacher>",
        TeahcerExpertyListView.as_view(),
        name="list_teacher_experty",
    ),
]
