from rest_framework import serializers

from school.models import ClassGrade, Experties, Teacher


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["name", "email", "phone_number"]


class ClassGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassGrade
        feilds = ["name"]


class ExpertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experties
        feilds = ["domain", "Teacher"]
