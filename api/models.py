from django.db import models


class Product(models.Model):
    image = models.ImageField()
    title = models.TextField()
    full_description = models.TextField()

    def __str__(self):
        return self.title

    
