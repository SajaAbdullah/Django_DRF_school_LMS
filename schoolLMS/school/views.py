from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Teacher
from .serializers import UserSerializer


class TeacherListApiView(APIView):
    def get(self, request):
        """
        List all Teachers
        """
        teachers = Teacher.objects.all()
        serializer = UserSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
