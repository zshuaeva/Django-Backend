from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required


@login_required
def list_projects(request):
    projects = Project.objects.filter(
        owner=request.user
    )
    context = {
        "project_list": projects,
    }
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
    project = Project.objects.get(id=id)
    context = {
        "project_object": project,
    }
    return render(request, "projects/show_project.html", context)
