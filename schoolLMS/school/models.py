import uuid

from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, default=" ")
    phone_regex = RegexValidator(
        regex="^((\\+92)?(0092)?(92)?(0)?)(3)([0-9]{9})$",
        message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.",
    )
    phone_number = models.PositiveIntegerField(validators=[phone_regex])


class Owner(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, default=" ")
    phone_regex = RegexValidator(
        regex="^((\\+92)?(0092)?(92)?(0)?)(3)([0-9]{9})$",
        message="Phone number must be entered in the format:"
        + " '+999999999'. Up to 12 digits allowed.",
    )
    phone_number = models.PositiveIntegerField(validators=[phone_regex])


class Student(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, default=" ")
    phone_regex = RegexValidator(
        regex="^((\\+92)?(0092)?(92)?(0)?)(3)([0-9]{9})$",
        message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.",
    )
    phone_number = models.PositiveIntegerField(validators=[phone_regex])


class ClassGrade(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50)


class TeacherClasses(models.Model):
    class meta:
        unique_together = (("class_grade", "teacher"),)

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    class_grade = models.ForeignKey(ClassGrade, on_delete=models.CASCADE)
    class_grade = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Experties(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    domain = models.CharField(max_length=50)
