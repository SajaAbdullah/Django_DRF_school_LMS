from django.test import TestCase
from django.urls import reverse
from ..serializers import UserSerializer
from ..views import TeacherCreateView

from ..models import Teacher
from ddt import ddt, data, unpack
@ddt
class TeacherTestCase(TestCase):

    @data(("saja", "asla@gmail.com", "032456974813"),
          ("abdi", "abdi@gmail.com", "038245652653"),
          ("farhan", "farhan@gmail.com", "032456974813"))
    @unpack
    def test_model_content(self,  name, email, phone_number):
        """test that inserted data from set up is inserted successfully"""
        Teacher.objects.create(name=name, email=email, phone_number=phone_number)

    def test_teacher_url_exists_at_correct_location(self):
        """test urls routes is correct and up for running"""
        response = self.client.get("/school/create_teacher/")
        self.assertEqual(response.status_code, 405)

    def test_api(self):
        """second method to check url is Exist"""
        response = reverse("school:create_teacher")
        self.assertEquals("/school/create_teacher/", response)

