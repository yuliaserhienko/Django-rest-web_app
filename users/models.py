from django.db import models
from django.contrib.auth.models import AbstractUser
from .enums import UserTypes


USER_TYPES = [
    (_type.value, _type.name) for _type in UserTypes
]


class User(AbstractUser):
    type = models.SmallIntegerField(
        choices=USER_TYPES, default=UserTypes.USER.value)
