from django.db import models

# Create your models here.
from users.models import User


class Kehamilan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ttl = models.DateField()
    hpht = models.DateField()
    hpl = models.DateField()

    def __str__(self):
        return self.user.name
