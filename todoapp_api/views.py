from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import TemplateView
from django.db.models import Q

from todoapp.models import ToDoNote, Comment
from . import serializers, filters, permissions
from Web_todoapp.settings_local import SERVER_VERSION

class AboutTemplateView(TemplateView):
    """Стартовая информация о сервере и пользователе"""
    template_name = "about.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["server_version"] = SERVER_VERSION
        context["user_name"] = self.request.user.username
        return context


class ToDoListApiView(generics.ListCreateAPIView):
    """ Отображение всех заметок с возможностью фильтрации """
    queryset = ToDoNote.objects.all()
    serializer_class = serializers.NoteSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.ToDoAppFilter

    def get_queryset(self):
        """Доступ к заметкам текущего пользователя и публичным заметкам других"""
        queryset = super().get_queryset()
        return queryset.filter(Q(author=self.request.user) | Q(public=True))

    def perform_create(self, serializer):
        """Перегружаем автора при сохранении заметок"""
        serializer.save(author=self.request.user)
        return serializer


class ToDoDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    """ Отображение и редактирование/удаление конкретной заметки """
    queryset = ToDoNote.objects.all()
    serializer_class = serializers.NoteSerializer
    permission_classes = [permissions.OnlyAuthorEdit & permissions.OnlyPublicRead & IsAuthenticated]

    def perform_update(self, serializer):
        """Метод для редактирования заметки"""
        return serializer.save()


class CommentListAPIView(generics.ListCreateAPIView):
    """Отображение и создание комментариев"""
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticated & permissions.OnlyPublicComment]

    def perform_create(self, serializer):
        """Создание комментария"""
        serializer.save(author=self.request.user)

        return serializer










