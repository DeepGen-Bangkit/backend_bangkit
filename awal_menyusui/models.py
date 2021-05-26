from django.db import models

# Create your models here.
from users.models import User


class Menyusui(models.Model):
    GENDER = (
        (0, "Laki Laki"),
        (1, "Perempuan")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    baby_name = models.CharField(max_length=255)
    ttl_baby = models.DateField()
    gender = models.IntegerField(choices=GENDER)
    length = models.FloatField()
    weight = models.FloatField()
    lingkar_kepala = models.FloatField()
    is_mpasi = models.BooleanField()

    def __str__(self):
        return self.baby_name
