from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from spa_tables.models import TableData
from spa_tables.serializers import TableDataSerializer


class TableDataViewSet(viewsets.ModelViewSet):
    queryset = TableData.objects.all()
    serializer_class = TableDataSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['name', 'quantity', 'distance']
    ordering = ['-date']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Фильтрация
        column = self.request.query_params.get('column')
        condition = self.request.query_params.get('condition')
        value = self.request.query_params.get('value')

        if column and condition and value:
            if column == 'name':
                if condition == 'equals':
                    queryset = queryset.filter(name=value)
                elif condition == 'contains':
                    queryset = queryset.filter(name__icontains=value)
            elif column in ['quantity', 'distance']:
                try:
                    if column == 'quantity':
                        field_value = int(value)
                    else:
                        field_value = float(value)

                    if condition == 'equals':
                        queryset = queryset.filter(**{f'{column}': field_value})
                    elif condition == 'greater':
                        queryset = queryset.filter(**{f'{column}__gt': field_value})
                    elif condition == 'less':
                        queryset = queryset.filter(**{f'{column}__lt': field_value})
                except (ValueError, TypeError):
                    pass

        return queryset
