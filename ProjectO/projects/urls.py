from django.urls import path, reverse_lazy

from . import (
    views as project_views,
)


app_name = 'projects'

urlpatterns = [
    path('software-projects/', project_views.software_projects, name='software_projects'),
]
