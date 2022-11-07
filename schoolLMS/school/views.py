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


class TeacherApiView(APIView):
    def get(self, request):
        """
        retrive teacher method using quary parms
        """
        teacher = Teacher.objects.filter(id=request.GET.get("uuid"))
        if not teacher:
            return Response(
                {"res": "Teacher does not exists"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = UserSerializer(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        save enterd data in teacher model
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        """
        update teacher data
        """
        teacher_instance = Teacher.objects.filter(id=request.data.get("id"))
        if not teacher_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = UserSerializer(
            instance=teacher_instance, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        Deletes teacher
        """
        teacher_instance = Teacher.objects.filter(id=request.GET.get("uuid"))
        if not teacher_instance:
            return Response(
                {"res": "Teacher does not exists"}, status=status.HTTP_404_NOT_FOUND
            )
        teacher_instance.delete()
        return Response({"res": "Teacher deleted!"}, status=status.HTTP_200_OK)
