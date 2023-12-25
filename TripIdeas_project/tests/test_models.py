from django.test import TestCase
from pytest import fixture as pytest_fixture
from datetime import datetime
import pytest

from app.models import PriceModelWithTracker


class TestPriceModelWithTracker(TestCase):
    min_price_in_history = 50
    max_price_in_history = 100

    @classmethod
    def setUpTestData(cls):
        test_price = PriceModelWithTracker.objects.create(price=cls.max_price_in_history)
        test_price.price = cls.min_price_in_history
        test_price.save()

    @pytest_fixture
    def test_price(self):
        return PriceModelWithTracker.objects.first()

    @pytest.mark.django_db
    def test_min_price_between_dates(self, test_price):
        start_date = datetime(2020, 1, 1).date()
        end_date = datetime.now()

        result_min_price = test_price.min_price_between_dates(start_date, end_date)
        expected_min_price = self.min_price_in_history

        self.assertEqual(expected_min_price, result_min_price)
