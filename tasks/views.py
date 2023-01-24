from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        form = form.save()
        return redirect("list_projects")
    else:
        form = TaskForm()
    context = {
        "form": form
    }
    return render(request, "create_task.html", context)
