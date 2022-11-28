import json

from ddt import data, ddt, unpack
from django.test import Client, TestCase
from django.urls import reverse

from ..models import Teacher


@ddt
class TeacherTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client()
        cls.teacher = Teacher.objects.create(
            name="Safwan", email="safwan@gmail.com", phone_number="030844631498"
        )

    def test_teacher_list_GET_api(self):
        """test teacher list api url and view"""

        response = self.client.get(reverse("school:list_teacher"))
        self.assertEquals(response.status_code, 200)

    def test_teacher_GET_api(self):
        """test retrieve teacher api by passing the id"""
        user = Teacher.objects.get(name="Safwan")
        response = self.client.get(reverse("school:retrieve_teacher", args=[user.id]))
        self.assertEquals(response.status_code, 200)

    @data(
        ("Adnan", "adnan@gmail.com", "03055789655"),
        ("abdi", "abdi@gmail.com", "03044896577"),
        ("farhan", "farhan@gmail.com", "03044698755"),
    )
    @unpack
    def test_teacher_POST_api(self, name, email, phone_number):
        """test post request api by passing multiple data"""
        response = self.client.post(
            reverse("school:create_teacher"),
            {"name": name, "email": email, "phone_number": phone_number},
        )
        print(response.data)
        self.assertEquals(response.status_code, 200)
