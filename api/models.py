from django.db import models


class User(models.Model):
    username = models.CharField(max_length=233)
    url = models.URLField(max_length=211)
    user_id = models.IntegerField(max_length=44)


class Product(models.Model):
    image = models.ImageField()
    title = models.TextField()
    full_description = models.TextField()

    def __str__(self):
        return self.title

    
