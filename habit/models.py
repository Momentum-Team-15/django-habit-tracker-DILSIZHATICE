from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint


# Create your models here.
class User(AbstractUser):
    pass

class Habit(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    measurement = models.PositiveIntegerField(null=True, blank=True)
    unit_of_measure = models.CharField(max_length=500, null=True, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f"{self.name} {self.measurement} {self.unit_of_measure}"


class Record(models.Model):
    habit_record = models.ForeignKey('Habit', on_delete=models.CASCADE, related_name='records', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    amount = models.IntegerField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['habit_record', 'date', 'amount'], name ='record_amount')
        ]

    def __str__(self):
        return f" Record for {self.habit.name}"


