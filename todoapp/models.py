from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE, default=1)