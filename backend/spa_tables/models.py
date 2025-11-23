from django.db import models


class TableData(models.Model):
    date = models.DateField(verbose_name="Дата")
    name = models.CharField(max_length=255, verbose_name="Название")
    quantity = models.IntegerField(verbose_name="Количество")
    distance = models.FloatField(verbose_name="Расстояние")

    class Meta:
        db_table = 'table_data'
        verbose_name = 'Данные таблицы'
        verbose_name_plural = 'Данные таблицы'
        ordering = ['-date']

    def __str__(self):
        return f"{self.name} - {self.date}"