from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ValidationError
from spa_tables.serializers import TableDataSerializer
from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from spa_tables.models import TableData


class TableTestCase(APITestCase):
    def setUp(self) -> None:
        self.table = TableData.objects.create(date='2025-10-15', name='Test', quantity=10, distance=1000)

    def test_tabledata_list(self):
        url = reverse("spa_tables:tabledata-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tabledata_retrieve(self):
        url = reverse("spa_tables:tabledata-detail", args=(self.table.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.table.name)
        self.assertEqual(data.get("quantity"), 10)

    def test_tabledata_create(self):
        url = reverse("spa_tables:tabledata-list")
        data = {
            "date": "2025-12-02",
            "name": "Moscow",
            "quantity": 5,
            "distance": 2500,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TableData.objects.all().count(), 2)

    def test_tabledata_update(self):
        url = reverse("spa_tables:tabledata-detail", args=(self.table.pk,))
        data = {
            "date": "2025-02-12",
            "name": "St.Peterburg",
            "quantity": 4,
            "distance": 1500,
        }
        response = self.client.patch(url, data=data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "St.Peterburg")
        self.assertEqual(data.get("distance"), 1500)

    def test_tabledata_delete(self):
        url = reverse("spa_tables:tabledata-detail", args=(self.table.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TableData.objects.all().count(), 0)
