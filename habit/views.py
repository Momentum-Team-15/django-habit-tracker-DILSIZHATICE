from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Habit, Record
from .forms import HabitForm, RecordForm

# Create your views here.
@login_required
def login(request):
    return render(request, 'accounts/login/')


def index (request):
    habits = Habit.objects.all()
    return render(request, 'habit/index.html', {'habits': habits})



def create_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST, request.FILES)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect("home")
    else:
        form = HabitForm()

    return render(request, 'habit/create_habit.html', {'form': form})    


def create_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save()
            return redirect("home")
    else:
        form = RecordForm()

    return render(request, 'habit/create_record.html', {'form': form})    


def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    records = Record.objects.all()
    return render(request,'habit/habit_detail.html',{'records':records,'habit':habit})





def habit_edit(request, habitpk):
    habit = get_object_or_404(Habit, pk=habitpk)
    if request.method == "POST":
        form = HabitForm(request.POST, request.FILES, instance=habit)
        if form.is_valid():
            habit = form.save()
            habit.created_at = timezone.now()
            habit.save()
            habit.user = request.user
            return redirect('home')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'habit/habit_edit.html', {'form': form})


def record_edit(request, recordpk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == "POST":
        form = RecordForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('home', pk=record.pk)
    else:
        form = RecordForm(instance=record)
    return render(request, 'habit/record_edit.html', {'form': form})
 

def habit_delete(request, habitpk):
    habit = Habit.objects.get(pk=habitpk)
    habit.delete()
    return redirect('home')   

def record_delete(request, recordpk):
    habit = Record.objects.get(pk=recordpk)
    record.delete()
    return redirect('home')  

