from django.urls import path

from .views import (
    ListTeacherClassView,
    ListTeahcerExperty,
    TeacherClassCreateView,
    TeacherCreateView,
    TeacherListView,
    TeacherRUDView,
)

app_name = "school"
urlpatterns = [
    path("list_teachers/", TeacherListView.as_view(), name="teachers_list_api"),
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
        "add_teacher_class/",
        TeacherClassCreateView.as_view(),
        name="add_teacher_class",
    ),
    path(
        "list_teacher_classes/",
        TeacherClassCreateView.as_view(),
        name="add_teacher_class",
    ),
    path(
        "list_teacher_classes/<uuid:teacher>",
        ListTeacherClassView.as_view(),
        name="list_teacher_classes",
    ),
    path(
        "list_teacher_experty/<uuid:teacher>",
        ListTeahcerExperty.as_view(),
        name="list_teacher_experty",
    ),
]
