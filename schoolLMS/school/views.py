from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

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


class TeacherCreateView(APIView):
    """
    create and add teacher object in DB
    """

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


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
    """method that lists teacher expertise from TeacherExperty class
    one to many field"""

    queryset = TeacherExperty.objects.all()
    serializer_class = TeacherExpertySerializer
    lookup_field = "teacher"
