from rest_framework import generics

from .models import Teacher, TeacherClass, TeacherExperty
from .serializers import (
    TeacherClassSerializer,
    TeacherExpertySerializer,
    UserSerializer,
)


class TeacherListView(generics.ListAPIView):
    """
    using generic views list teachers
    """

    queryset = Teacher.objects.all()
    serializer_class = UserSerializer


class TeacherCreateView(generics.CreateAPIView):
    """
    Save teacher object in DB
    """

    queryset = Teacher.objects.all()
    serializer_class = UserSerializer


class TeacherRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    combind Retrieve/Update/Delete into one view
    """

    queryset = Teacher.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"


class TeacherClassCreateView(generics.CreateAPIView):
    """
    add teacher classes
    """

    queryset = TeacherClass.objects.all()
    serializer_class = TeacherClassSerializer


class ListTeacherClassView(generics.ListAPIView):
    """
    using generic views list teachers
    """

    queryset = TeacherClass.objects.all()
    serializer_class = TeacherClassSerializer
    lookup_field = "teacher"


class ListTeahcerExperty(generics.ListAPIView):

    queryset = TeacherExperty.objects.all()
    serializer_class = TeacherExpertySerializer
    lookup_field = "teacher"
