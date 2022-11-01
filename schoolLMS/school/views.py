import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Teacher

# Create your views here.


class UserEncoder(json.JSONEncoder):
    def default(self, user):
        if isinstance(user, Teacher):
            return {
                "name": user.name,
                "email": user.email,
                "phone Number": user.phone_number,
            }
        return super().default(user)


class ListTeacherView(View):

    # list of objects return
    def get(self, request):
        """
        retirive all teachers of database and return them
        """
        teachers = Teacher.objects.all()
        serilizedTeachers = []
        for teacher in teachers:
            serilizedTeachers.append(json.loads(json.dumps(teacher, cls=UserEncoder)))
        return JsonResponse({"All teachers": serilizedTeachers})


@method_decorator(csrf_exempt, name="dispatch")
class SingleTeacherView(View):

    # single object return
    def get(self, request, uuid):
        """
        this method take http request of get type of single
        teacher by id, retrieve the specified teacher according
        id and return response in json format
        """
        teacher = Teacher.objects.get(id=uuid)
        serilized = json.dumps(json.loads(teacher, cls=UserEncoder))
        return JsonResponse({"teacher": serilized})

    def post(self, request, format=None):
        """
        take post http request with json body
        ,save object to DB and return saved data
        """
        teacher = json.loads(request.body)
        Teacher.objects.create(**teacher)
        return JsonResponse({"teacher": teacher})
