from django.contrib import admin

from .models import ToDoNote


# Связь админки с моделью
@admin.register(ToDoNote)
class ToDoNoteAdmin(admin.ModelAdmin):

    # Прописать конкретные поля и последовательность
    list_display = ('title', 'note_status', 'public', 'importance', 'author')

    # Как групировать поля в модели в админке по другому
    fields = (('title', 'public', 'importance'), 'note_status', 'author', 'message', 'create_at', 'deadline_time')

    # Поля, которые хотим видеть, но только в режиме чтения
    readonly_fields = ('create_at', 'deadline_time')

    # Хотим что-то искать, указываем по каким полям
    search_fields = ['title', 'message']

    # Хотим уметь фильтровать записи по какому-то полю
    list_filter = ['public', 'note_status']
