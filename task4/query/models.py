from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    count=models.IntegerField(default=0)

    def __str__(self):
        return self.username