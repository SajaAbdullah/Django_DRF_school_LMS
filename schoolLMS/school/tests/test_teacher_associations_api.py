from django.test import TestCase
from django.urls import reverse

from ..models import ClassGrade, Teacher, TeacherExperty


class TestTeacherAssociationsAPi(TestCase):
    @classmethod
    def setUpTestData(cls):
        """setting up users for testing"""
        cls.class_grade_one = ClassGrade.objects.create(name="Grade One")
        cls.class_grade_two = ClassGrade.objects.create(name="Grade Two")
        cls.class_grade_three = ClassGrade.objects.create(name="Grade Three")

        cls.teacher = Teacher.objects.create(name="saja", phone_number="030844631498")

        cls.teacher_experty = TeacherExperty.objects.create(
            domain="math", teacher=cls.teacher.id
        )

    def test_create_teacherClasses(self):
        """tests post request api of adding teacher class"""
        response = self.client.post(
            reverse("school:create_teacher_class"),
            {"teacher": self.teacher.id, "class_grade": self.class_grade_one.id},
        )
        self.assertEqual(response.status_code, 201)

    def test_list_teacher_Classes(self):
        """tests list/get request api passing teacher id"""
        response = self.client.get(
            reverse("school:list_teacher_classes", args=[self.teacher.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_list_teacher_Classes(self):
        """tests list/get teacher many experties api passing teacher id"""
        response = self.client.get(
            reverse("school:list_teacher_experty", args=[self.teacher.id])
        )
        self.assertEqual(response.status_code, 200)
