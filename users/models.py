from django.contrib.auth.models import AbstractUser
from django.db import models
from allauth.account.models import EmailAddress


class User(AbstractUser):
    PHASE = (
        (0, "KEHAMILAN"),
        (1, "AWAL MENYUSUI"),
        (2, "MPASI")
    )
    username = models.CharField(null=True, blank=True, max_length=200)
    name = models.CharField(blank=True, max_length=255)
    phase = models.IntegerField(default=0, choices=PHASE)
    date_birth = models.DateField(null=True)

    def __str__(self):
        return "%s - %s" % (self.username, self.name)

    def clean_email(self):
        EmailAddress.objects.get_or_create(user=self, email=self.email, primary=True, verified=True)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        self.clean_email()
