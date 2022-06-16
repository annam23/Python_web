from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta


def deadline_datetime():
    "Заметка должна иметь дату и время, по умолчанию +1 день от текущего, может быть изменена автором"
    return datetime.now() + timedelta(days=1)


class ToDoNote(models.Model):
    """Описывает наполнение заметки"""

    class NoteStatus(models.IntegerChoices):
        """ Описывает статус заметки"""
        DELAYED = 0, _("Отложено")
        ACTIVE = 1, _("Активно")
        DONE = 2, _("Выполнено")

    note_status = models.IntegerField(default=NoteStatus.ACTIVE,
                                      choices=NoteStatus.choices,
                                      verbose_name='Статус')
    title = models.CharField(max_length=300, verbose_name='Заметка')
    message = models.TextField(default='', verbose_name='Описание заметки')
    importance = models.BooleanField(default=False, verbose_name='Важно')
    public = models.BooleanField(default=False, verbose_name='Публичная')
    create_at = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    deadline_time = models.DateTimeField(default=deadline_datetime, verbose_name='Срок выполнения')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        "Отображение человекочитаемой записи объекта в админке"
        return f"Заметка №{self.id}"

    class Meta:
        ordering = ['create_at', 'importance']
        verbose_name = _('заметка')
        verbose_name_plural = _('заметки')


class Comment(models.Model):
    """Класс для комментариев заметок"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    comment_note = models.ForeignKey(ToDoNote, on_delete=models.CASCADE, verbose_name='Заметка')
    comment = models.CharField(max_length=150, null=False, verbose_name='Комментарий')

    class Meta:
        verbose_name = _('комментарий')
        verbose_name_plural = _('комментарии')


