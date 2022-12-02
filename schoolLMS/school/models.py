import uuid

from django.core.validators import RegexValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Teacher(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4
    )
    name = models.CharField(max_length=50)
    phone_number = models.CharField(
        null=True,
        blank=True,
        max_length=17,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Phone number format: '+999999999'.",
            )
        ],
    )


class Student(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, default=" ")
    phone_number = models.CharField(
        null=True,
        blank=True,
        max_length=17,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Phone number format: '+999999999'.",
            )
        ],
    )
    class_grade = models.UUIDField(editable=True, default=uuid.uuid4)


class ClassGrade(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50)


class TeacherClass(models.Model):
    class Meta:
        unique_together = (("class_grade", "teacher"),)

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    class_grade = models.UUIDField(editable=True, default=uuid.uuid4)
    teacher = models.UUIDField(editable=True, default=uuid.uuid4)


class TeacherExperty(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    teacher = models.UUIDField(editable=True, default=uuid.uuid4)
    domain = models.CharField(max_length=50)
