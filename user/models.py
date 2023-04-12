from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse_lazy


class UserModel(AbstractUser):
    img = models.ImageField(
        upload_to='user/img',
        default='user/img/user_img.png'
    )

    email = models.EmailField(
        unique=True
    )

    money = models.FloatField(
        default=10000
    )

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "користувач"
        verbose_name_plural = "користувачі"

    def get_absolute_url(self):
        return reverse_lazy('user:profile_url')
