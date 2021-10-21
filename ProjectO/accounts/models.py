from django.db import models
from django.contrib.auth import models


# user model
class User(models.User, models.PermissionsMixin):

    def __str__(self):
        return f"@{self.username}"
