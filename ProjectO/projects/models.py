from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


class Post(models.Model):
    """ Project Post model """
    project_name = models.CharField(max_length=100)
    project_type = models.CharField(max_length=20, default='other', blank=False, unique=False)
    project_requirement = models.TextField()
    project_description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)    # User model relation

    def __str__(self):
        return f"{self.project_name}"

