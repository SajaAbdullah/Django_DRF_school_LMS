from rest_framework import serializers

from .models import ClassGrade, Teacher, TeacherClass, TeacherExperty


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "name", "phone_number"]

    def validate(self, data):
        name = data.get("name")
        teachers = Teacher.objects.all()
        for t in teachers:
            if t.name == name:
                raise serializers.ValidationError("name must be unique ^_^")
        return data


class ClassGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassGrade
        fields = ["name"]


class TeacherClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherClass
        fields = ["class_grade", "teacher"]


class TeacherExpertySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherExperty
        fields = ["domain"]
