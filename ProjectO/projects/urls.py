from django.urls import path, reverse_lazy

from . import (
    views as project_views,
)


app_name = 'projects'

urlpatterns = [
    path('creative-projects/', project_views.creative_projects, name='creative_projects'),
    path('electronics-projects/', project_views.electronics_projects, name='electronics_projects'),
    path('software-projects/', project_views.software_projects, name='software_projects'),
]
