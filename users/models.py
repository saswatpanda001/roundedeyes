from django.db import models
import uuid
from django.utils import timezone


class UserContactData(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    key = models.CharField(max_length=20, blank=True, null=True, default="")
    time = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self.key == "":
            self.key = str(uuid.uuid4())[:16]
        return super().save(*args, **kwargs)

    def __str__(self):
        return (self.name)
