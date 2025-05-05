from django.db import models

class Author(models.Model):
    name = models.CharField("Имя", max_length=100)
    bio = models.TextField("Биография")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def parse_object(self):
        return {
            "id": self.id,
            "name": self.name,
        }

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

class Review(models.Model):
    name = models.CharField("Имя или никнейм", max_length=30)
    message = models.TextField("Сообщение")
    date_create = models.DateTimeField("Дата добавления", auto_now_add=True)



    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class User(models.Model):
    name = models.CharField("Имя", max_length=50)
    age = models.IntegerField("Возраст")

    reviews = models.ForeignKey(Review, related_name="reviews", verbose_name="Отзыв(ы)", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

        