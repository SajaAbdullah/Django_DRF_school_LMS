from ddt import data, ddt, unpack
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from ..models import Teacher


@ddt
class TestTeacherAPi(TestCase):
    @classmethod
    def setUpTestData(cls):
        """setting up users for testing"""
        cls.teacher = Teacher.objects.create(name="safwan", phone_number="030844631498")

    def test_teacher_retrieve_api(self):
        """tests retrieve teacher api by passing the id"""
        response = self.client.get(
            reverse("school:retrieve_teacher", args=[self.teacher.id])
        )
        self.assertEqual(response.data["name"], "safwan")
        self.assertEqual(response.status_code, 200)

    def test_teacher_list_api(self):
        """tests list all teachers api"""
        response = self.client.get(reverse("school:list_teacher"))
        self.assertEqual(response.status_code, 200)

    @data(
        ("adnan", "030557896552"),
        ("faheem", "030557898875"),
    )
    @unpack
    def test_create_teacher_pass(self, name, phone_number):
        """tests post request api by passing correct data"""
        response = self.client.post(
            reverse("school:create_teacher"),
            {"name": name, "phone_number": phone_number},
        )
        self.assertEqual(response.status_code, 201)

    @data(
        ("adnan", "096552"),
        ("safwan", "030557898875"),
    )
    @unpack
    def test_create_teacher_fail(self, name, phone_number):
        """tests post request api by passing wrong data"""
        response = self.client.post(
            reverse("school:create_teacher"),
            {"name": name, "phone_number": phone_number},
        )
        self.assertEqual(response.status_code, 400)

    def test_update_teacher(self):
        """tests update request api"""
        client = APIClient()
        response = client.put(
            reverse("school:update_teacher", args=[self.teacher.id]),
            {"name": "Hasan", "phone_number": "032456975125"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Hasan")

    def test_delete_teacher(self):
        """tests delete request api"""
        response = self.client.delete(
            reverse("school:update_teacher", args=[self.teacher.id])
        )
        self.assertEqual(response.status_code, 204)
