from django.forms import ModelForm
from projects.models import Project


class CreateProject(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "owner",
        ]
