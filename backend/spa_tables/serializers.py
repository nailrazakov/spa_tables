from rest_framework import serializers
from spa_tables.models import TableData

class TableDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableData
        fields = ['id', 'date', 'name', 'quantity', 'distance']
