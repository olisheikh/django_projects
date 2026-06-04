from django.db import models
from todo.models import TrackableModel
# Create your models here.
class Tasks(TrackableModel):
    task_name = models.CharField(max_length=25)
    