from unittest.mock import Mock, patch

from django.test import TestCase

from ..views import TeacherCreateView


class TeacherTestCase(TestCase):
    def setUp(self):
        self.views = TeacherCreateView()
        self.json_data = {
            "name": "Safwan",
            "email": "saf@gmail.com",
            "phone_number": "03000844631498",
        }

    def test_post_teacher(self):
        with patch("school.views.TeacherCreateView.post") as mocked_create:
            mocked_create.return_value.data = {"key": "value"}

            created = self.views.post(Mock(data=self.json_data))
            print(created.status_code)
            print(created.data)
