from django.shortcuts import render

from .models import Post


def software_projects(request):
    """ List all software projects """
    context = {
        'posts': Post.objects.all(),
    }

    return render(request, 'projects/software_projects.html', context=context)