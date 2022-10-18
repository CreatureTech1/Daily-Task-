# tasks/models.py

from django.db import models


class Status(models.TextChoices):
    UNSTARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"


class Task(models.Model):
    name = models.CharField(verbose_name="Task name", max_length=65, unique=True)
    status = models.CharField(verbose_name="Task status", max_length=1, choices=Status.choices)

    def __str__(self):
        return self.name

from django import forms

# tasks/forms.py
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"
