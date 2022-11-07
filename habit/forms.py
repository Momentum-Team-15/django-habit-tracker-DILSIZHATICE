from django import forms
from .models import Habit, Record

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'measurement', 'unit_of_measure', 'user']
        

class RecordForm(forms.ModelForm):
     class Meta:
        model = Record
        fields = ['habit_record', 'amount', 'date']



        