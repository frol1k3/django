from django.db import models

class Author(models.Model):
    name = models.CharField("Имя", max_length=100)
    bio = models.TextField("Биография")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Book(models.Model):
    title = models.CharField("Название", max_length=70)
    desc = models.TextField("Описание")
    price = models.FloatField("Цена")
    date_public = models.DateField("Дата публикации")

    date_create = models.DateTimeField("Дата добавления", auto_now_add=True)
    date_edit = models.DateTimeField("Дата редактирования", auto_now=True)

    authors = models.ManyToManyField(Author, related_name="books", verbose_name="Автор(ы)")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"