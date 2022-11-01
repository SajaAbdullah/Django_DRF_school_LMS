from django.contrib import admin

from .models import ClassGrade, Owner, Student, Teacher

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Owner)
admin.site.register(Student)
admin.site.register(ClassGrade)
