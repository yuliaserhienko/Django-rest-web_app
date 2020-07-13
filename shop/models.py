from django.db import models
from users.models import User


class Shop(models.Model):
    shop_id = models.PositiveIntegerField(primary_key=True)
    shop_name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name='shops', on_delete=models.CASCADE)

    def __str__(self):
        return self.shop_name
