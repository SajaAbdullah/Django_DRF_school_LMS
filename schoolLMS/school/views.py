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
    def get(self, request):
        """
        this method take http request of get type with quary parms
        urls "teacher/?uuid=f7d2ce46-c60b-44ec-b0c9-1978dea2b7e6"
        retrieve the specified teacher according uuid and return
        response in json format
        """
        teacher = Teacher.objects.get(id=request.GET["uuid"])
        serilized = json.loads(json.dumps(teacher, cls=UserEncoder))
        return JsonResponse({"teacher": serilized})

    def post(self, request):
        """
        take post http request with json body
        ,save object to DB and return saved data
        """
        teacher = json.loads(request.body)
        teachers = Teacher.objects.all()
        for t in teachers:
            if t.name == teacher["name"]:
                return JsonResponse(
                    {"teacher": "Teacher name is not unique."}, status=409
                )

        Teacher.objects.create(**teacher)
        return JsonResponse({"teacher": teacher})

    def put(self, request):
        """
        update method using put request, body type:raw json
        """
        body = json.loads(request.body)
        teacher = Teacher.objects.get(id=body.get("id"))
        teacher.name = body.get("name")
        teacher.email = body.get("email")
        teacher.phone_number = body.get("phone_number")

        serilized = json.loads(json.dumps(teacher, cls=UserEncoder))
        return JsonResponse({"Updated Teacher Data": serilized}, status=200)
    
    def delete(self, request):
        """
        delete method using delete request using id send using quary parms
        """
        teacher = Teacher.objects.get(id=request.GET.get("uuid"))
        teacher.delete()
        return JsonResponse( {"teacher":"deleted"} ,status=200)
