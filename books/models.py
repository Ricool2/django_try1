from cgitb import text
from pyexpat import model
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название', max_length = 50)
    author = models.CharField('Автор', max_length = 200)
    text = models.TextField('Текст книги')
    date = models.DateField('Дата публикации')

    #Специальный настраимаевый вывод
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return f'/books/{self.id}'
    
    #Класс обслуживания таблицы
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'