from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    