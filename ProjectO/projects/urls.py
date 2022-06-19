from django.urls import path, reverse_lazy

from . import (
    views as project_views,
)


app_name = 'projects'

urlpatterns = [
    path('creative-projects/', project_views.creative_projects,
         name='creative_projects'),
    path('electronics-projects/', project_views.electronics_projects,
         name='electronics_projects'),
    path('software-projects/', project_views.software_projects,
         name='software_projects'),
    path('add/new/',
         project_views.AddProjectView.as_view(
             template_name='projects/add_project_page.html'
         ),
         name='add_new_project'
         )
    # path('/detail')
]
