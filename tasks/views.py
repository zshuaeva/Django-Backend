from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        form = form.save()
        return redirect("list_projects")
    else:
        form = TaskForm()
    context = {"form": form}
    return render(request, "create_task.html", context)


@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {"task_list": tasks}
    return render(request, "show_my_tasks.html", context)
