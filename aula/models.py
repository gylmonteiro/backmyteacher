from tkinter import CASCADE
from django.db import models
from teacher.models import Professor
# Create your models here.
class Aula(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    professor = models.ForeignKey(to=Professor, on_delete=models.CASCADE, related_name="aulas", null=False, blank=False)