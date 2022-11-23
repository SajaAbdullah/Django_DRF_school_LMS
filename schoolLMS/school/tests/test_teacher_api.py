from django.test import TestCase
from django.urls import reverse

from ..models import Teacher


class TeacherTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """this function set up the data in virtual DB to check its insertion
        Simple setUp execute many times with each function.
        using setUpTestData(cls) will execute once for whole TestCase class"""
        cls.teacher = Teacher.objects.create(
            name="sana", email="sana@gmail.com", phone_number="03044635411"
        )

    def test_model_content(self):
        """test that inserted data from set up is inserted successfully"""
        teacher = Teacher.objects.get(name="sana")
        self.assertEquals(teacher.name, "sana")
        self.assertEquals(teacher.email, "sana@gmail.com")
        self.assertEqual(str(teacher.phone_number), "3044635411")

    def test_teacher_url_exists_at_correct_location(self):
        """test urls routes is correct and up for running"""
        response = self.client.get("/school/create_teacher/")
        self.assertEqual(response.status_code, 405)

    def test_api(self):
        """second method to check url is Exist"""
        response = reverse("school:create_teacher")
        self.assertEquals("/school/create_teacher/", response)
