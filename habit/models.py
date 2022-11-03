from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass

class Habit(models.Model):
    title = models.CharField(max_length=200)
    name = models.ForeignKey('Name', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f"{self.title} by {self.name}"


class Name(models.Model):
    userName = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.userName}"