from django.db.models import Count, Avg, Min, Max, Q

from todoapp.models import ToDoNote


def notes_count():
    """Функция для вычисление кол-ва записей"""
    return ToDoNote.objects.all().count()


def notes_count_position():
    """Функция для вычисление кол-ва записей по определенному полю"""
    return ToDoNote.objects.aggregate(Count("id"))


def notes_describe_public():
    """Вывести сводную инф-цию по публичным и непубличным заметкам"""
    published = Count("public", filter=Q(public=True))
    unpublished = Count("public", filter=Q(public=False))
    return ToDoNote.objects\
        .aggregate(
            published=published,
            unpublished=unpublished
        )
