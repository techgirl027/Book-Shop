from django.db import models

# Create your models here.


class Images(models.Model):
    image = models.ImageField()


class Quotes(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=255)
    title = models.TextField()

    def __str__(self) -> str:
        return self.name


class Trend_books(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.full_name
