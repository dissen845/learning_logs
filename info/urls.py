"""Определяет схемы URL нашего приложения"""

from django.urls import path
from . import views

app_name = 'info'
urlpatterns = [
    #Домашняя страница
    path('', views.index, name='index'),
    #Страница со списком тем
    path('topics/', views.topics, name='topics'),
    #Страница со списком фильмов/сериалов и т.д.
    path('topics/<int:topic_id>/', views.titles, name='titles'),
    #Страница с комментарием к объекту
    path('topics/topic/<int:titles_id>/', views.discussion, name='discussion'),
    #Страница с созданием нового раздела
    path('new_topic/', views.new_topic, name='new_topic'),
    #Страница с созданием нового заголовка в разделе
    path('new_titles/<int:topic_id>/', views.new_titles, name='new_titles'),
    #страница с добавлением обсуждения
    path('new_discussion/<int:titles_id>/', views.new_discussion, name='new_discussion'),
    #редактирование заголовков
    path('edit_titles/<int:titles_id>/', views.edit_titles, name='edit_titles'),
    #Редактирование отзывов
    path('edit_discussion/<int:discussion_id>/', views.edit_discussion, name='edit_discussion'),
    #Удаления отзыва
    path('topics/topic/<int:discussion_id>/delite_discussion/', views.Delite.as_view(), name='delite_discussion'),
]
