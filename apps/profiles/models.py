from django.db import models

from django.contrib.auth import get_user_model

from apps.utils.helpers import avatar_upload_path

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to=avatar_upload_path, null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def get_avatar(self):
        if not self.avatar:
            return "/static/images/default.jpeg"
        else:
            return self.avatar.url
