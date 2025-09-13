from django.db import models
from datetime import date


class Todo(models.Model):
    job = models.CharField(max_length=100)
    deadline = models.DateField()
    created = models.DateField(auto_now_add=True)
    done = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Teendők"

    def __str__(self):
        return f"{self.job}"

