from django.db import models


class User(models.Model):
    username = models.CharField(max_length=233)
    url = models.URLField()
    user_id = models.IntegerField()


class Product(models.Model):
    image = models.ImageField()
    title = models.TextField()
    full_description = models.TextField()

    def __str__(self):
        return self.title


class Todo(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
