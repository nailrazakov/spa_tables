from django.core.management.base import BaseCommand
from django.utils import timezone
from spa_tables.models import TableData
import random
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Fill database with random data'

    def handle(self, *args, **options):
        names = [
            "Проект Альфа", "Проект Бета", "Проект Гамма",
            "Проект Дельта", "Проект Эпсилон", "Проект Зета",
            "Проект Эта", "Проект Тета", "Проект Йота"
        ]

        TableData.objects.all().delete()

        data_list = []
        for i in range(100):
            date = timezone.now().date() - timedelta(days=random.randint(0, 365))
            name = random.choice(names) + f" {random.randint(1, 100)}"
            quantity = random.randint(1, 1000)
            distance = round(random.uniform(1.0, 1000.0), 2)

            data_list.append(TableData(
                date=date,
                name=name,
                quantity=quantity,
                distance=distance
            ))

        TableData.objects.bulk_create(data_list)
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {len(data_list)} records')
        )
