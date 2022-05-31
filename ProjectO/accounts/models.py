from django.db import models
from django.contrib.auth import models as auth_models


# user model
class User(auth_models.User, auth_models.PermissionsMixin):
    def __str__(self):
        return f"@{self.username}"


class Profile(models.Model):
    """ User profile class """
    user = models.OneToOneField(auth_models.User, null=True, on_delete=models.CASCADE)
    profile_image = models.ImageField(default="default.jpg", upload_to='profile_pics')
    profile_description = models.CharField(blank=True, null=True, max_length=500)
    collage_name = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return f"{self.user} Profile"
