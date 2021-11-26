from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Разделы(фильмы, сериалы и т.д.)"""
    text = models.CharField('Раздел', max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=40, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        """Возвращает строковое значение модели"""
        return self.text

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

class Titles(models.Model):
    """перечисление того, что попало в раздел"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField('Контент', max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Контент'

    def __str__(self):
        """Возвращает строковое значение модели"""
        return self.text

class Discussion(models.Model):
    """обсуждение данного контента"""
    topic = models.ForeignKey(Titles, on_delete=models.CASCADE)
    text = models.TextField('Отзыв')
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        """Возвращает строковое значение модели"""
        if len(self.text) <= 50:
            return self.text
        else:
            return f"{self.text[:50]}..."

