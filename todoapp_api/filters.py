from django_filters import rest_framework as filters

from todoapp.models import ToDoNote


class ToDoAppFilter(filters.FilterSet):
    """Класс для фильтрации по статусу, публичности и важности"""
    # Возможность фильтрации заметок с несколькими статусами
    multiply_choice = filters.AllValuesMultipleFilter(
        field_name='note_status',
        lookup_expr='in',
            )

    class Meta:
        model = ToDoNote
        fields = ['public', 'importance', 'multiply_choice']