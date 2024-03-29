from django.db import models
from projects.models import Project
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    is_completed = False
    project = models.ForeignKey(
        Project,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    assignee = models.ForeignKey(
        User,
        null=True,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
