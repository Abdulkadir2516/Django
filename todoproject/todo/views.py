from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form})

def task_edit(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_form.html', {'form': form})

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('task_list')

def task_complete(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = not task.completed  # Tamamlanma durumunu tersine çevir
    task.save()
    return redirect('task_list')
