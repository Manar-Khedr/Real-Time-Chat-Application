from django.contrib.auth.models import User
from django.db import models

class ActiveUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40)