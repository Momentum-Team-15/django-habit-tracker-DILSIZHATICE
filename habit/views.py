from django.shortcuts import render, get_object_or_404
from .models import Habit

# Create your views here.
def index (request):
    habits = Habit.objects.all()
    return render(request, 'habit/index.html', {'habits': habits})