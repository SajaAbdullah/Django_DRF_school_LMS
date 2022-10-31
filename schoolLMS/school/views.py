from django.shortcuts import render
from django.views import View
from .models import Teacher 
from django.http import JsonResponse
from .serializer import UserSerializer
import json

# Create your views here.

""" #using encoder function
def userEncoder(user):
   if isinstance(user ,Teacher):
      return {'name':user.name , 'email':user.email , 'phone Number':user.phoneNumber}

   raise TabError(f'Object {user} is not type of Teacher.')
 """
class UserEncoder(json.JSONEncoder):
   def default(self , user):
      if isinstance(user , Teacher):
         return {'name':user.name , 'email':user.email , 'phone Number':user.phoneNumber}
      
      return super().default(user)


class TeacherView(View):
   
   """ #single object return
   def get(self, request , uuid):
      teacher = Teacher.objects.get(id=uuid)
      print (teacher.name)
      serilized = json.dumps(teacher , cls=UserEncoder , indent=4)
      print (serilized)
      return JsonResponse({'teacher': serilized})
 """
   #single object return
   def get(self, request):
      teachers = Teacher.objects.all()

      serilizedTeachers=[] 
      for teacher in teachers:
         serilizedTeachers.append (json.loads( json.dumps(teacher , cls=UserEncoder )))

      return JsonResponse({'All teachers': serilizedTeachers})


    
