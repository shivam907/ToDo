from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=1000)
    completed = models.BooleanField()

