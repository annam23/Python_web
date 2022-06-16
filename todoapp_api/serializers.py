from rest_framework import serializers
from todoapp.models import ToDoNote, Comment


class NoteSerializer(serializers.ModelSerializer):
    """Сериализация задач"""

    author = serializers.SlugRelatedField(
        slug_field="username",
        # указываем новое поле(username or email, например) для визуализации вместо первоначального (pk, например)
        read_only=True
    )

    class Meta:
        model = ToDoNote
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """Сериализация комментариев"""

    class Meta:
        model = Comment
        fields = "__all__"
