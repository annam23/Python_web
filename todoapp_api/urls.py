from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('notes/', views.ToDoListApiView.as_view()),
    path('notes/<int:pk>', views.ToDoDetailApiView.as_view()),
    path('comments/', views.CommentListAPIView.as_view()),
    path('about/', views.AboutTemplateView.as_view()),

    ]