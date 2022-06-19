from django import forms

from .models import Post
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    """Form to add new project"""
    class Meta:
        model = Post
        fields = (
            'project_name', 'project_type', 'project_requirement',
            'project_description'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['project_name'].widget.attrs['class'] = 'bg-dark text-white'
        self.fields['project_name'].widget.attrs['placeholder'] = 'Enter Project Name'

        self.fields['project_type'].widget.attrs['class'] = 'bg-dark text-white'
        self.fields['project_type'].widget.attrs['placeholder'] = 'eg. software or creative or electronics'

        self.fields['project_requirement'].widget.attrs['class'] = 'bg-dark text-white'
        self.fields['project_requirement'].widget.attrs['placeholder'] = 'Enter Tech Requirements'
        self.fields['project_requirement'].widget.attrs['rows'] = 3

        self.fields['project_description'].widget.attrs['class'] = 'bg-dark text-white'
        self.fields['project_description'].widget.attrs['placeholder'] = 'Fill Project Description'
        self.fields['project_description'].widget.attrs['rows'] = 5
        # self.fields['author'].widget.attrs['class'] = 'bg-dark text-white'

    def project_name_clean(self):
        project_name = self.cleaned_data.get('project_name').lower()
        return project_name

    def project_type_clean(self):
        project_type = self.cleaned_data.get('project_type').lower()
        type_choice = ['software', 'creative', 'electronics']
        if project_type not in type_choice:
            project_type = "other"
        return project_type

    def project_requirement_clean(self):
        project_requirement = self.cleaned_data('project_requirement').lower()
        return project_requirement

    def project_description_clean(self):
        project_description = self.cleaned_data('project_description').lower()
        return project_description

    # def save(self, commit=False):
    #     user = User
    #     post = Post(
    #         project_name=self.cleaned_data['project_name'],
    #         project_type=self.cleaned_data['project_type'],
    #         project_requirement=self.cleaned_data['project_requirement'],
    #         project_description=self.cleaned_data['project_description'],
    #         author=self.request.user,
    #     )
    #     post.save(commit=True)
    #     return post

