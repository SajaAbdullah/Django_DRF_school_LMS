from django.contrib import admin
from .models import Teacher , Owner , Student ,ClassGrade
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Owner)
admin.site.register(Student)
admin.site.register(ClassGrade)