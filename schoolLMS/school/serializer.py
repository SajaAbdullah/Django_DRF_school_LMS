from rest_framework import serializers
from .models import Teacher , ClassGrade

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields =  "__all__"
  
