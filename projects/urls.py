from django.urls import path
from projects.views import list_projects, show_project, create_project


urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("create/", create_project, name="create_project"),
    path("<int:id>/", show_project, name="show_project"),

]
