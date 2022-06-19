from django.shortcuts import render

from .models import Post


def creative_projects(request):
    """ List all creative projects """
    creative_projects = Post.objects.filter(project_type="creative").all()
    other_projects = Post.objects.filter(project_type="other").all()
    context = {
        'posts': creative_projects,
        'other_posts': other_projects,
    }

    return render(request, 'projects/creative_projects.html', context=context)


def electronics_projects(request):
    """ List all electronics projects """
    context = {
        'posts': Post.objects.filter(project_type="electronics").all(),
    }

    return render(request, 'projects/electronics_projects.html', context=context)


def software_projects(request):
    """ List all software projects """
    context = {
        'posts': Post.objects.filter(project_type="software").all(),
    }

    return render(request, 'projects/software_projects.html', context=context)