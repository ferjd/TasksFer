from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib.auth.models import User
from django.db.models import Q

@login_required
def task_list(request):
    tasks = Task.objects.filter(Q(created_by=request.user) | Q(delegated_to=request.user)).order_by('-urgency', '-importance')
    status_choices = Task.STATUS_CHOICES
    priority_choices = Task.PRIORITY_CHOICES

    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        delegated_to_id = request.POST.get('delegated_to')

        if task_id and delegated_to_id:
            task = Task.objects.get(pk=task_id)
            delegated_to = User.objects.get(pk=delegated_to_id)
            task.delegated_to = delegated_to
            task.save()

    users = User.objects.exclude(pk=request.user.pk)  # Obtén la lista de usuarios disponibles para delegar

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'status_choices': status_choices, 'priority_choices': priority_choices, 'users': users})


@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        user = request.user  # Obtener el usuario actual
        task = Task.objects.create(title=title, created_by=request.user)  # Asignar el usuario a la tarea
        return redirect('task_list')
    return render(request, 'tasks/create_task.html')

def update_status(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        task.status = status
        task.save()
    return redirect('task_list')

def update_importance(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        importance = request.POST.get('importance')
        task.importance = importance
        task.save()
    return redirect('task_list')

def update_urgency(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        urgency = request.POST.get('urgency')
        task.urgency = urgency
        task.save()
    return redirect('task_list')

def update_observations(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        observations = request.POST.get('observations')
        task.observations = observations
        task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')


