from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from django.views.generic import (CreateView, DetailView)

from .models import Post
from .forms import PostForm


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


class PostDetailView(DetailView):
    model = Post


class AddProjectView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    redirect_field_name = '/accounts/profile/'

    form_class = PostForm
    model = Post

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddProjectView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return HttpResponseRedirect(self.redirect_field_name)