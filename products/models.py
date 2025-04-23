from django.db import models

class Author(models.Model):
    name = models.CharField("Имя", max_length=100)
    bio = models.TextField("Биография")


class Book(models.Model):
    title = models.CharField("Название", max_length=70)
    desc = models.TextField("Описание")
    price = models.FloatField("Цена")
    date_public = models.DateField("Дата публикации")

    date_create = models.DateTimeField("Дата добавления", auto_now_add=True)
    date_edit = models.DateTimeField("Дата редактирования", auto_now=True)

    authors = models.ManyToManyField(Author, related_name="books", verbose_name="Автор(ы)")