from django.db import models
from django.db.models.fields import related

# Create your models here.


class Priority(models.Model):
    name = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    description = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(blank=True, null=True, default=None)
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE, related_name="todo_items", blank=True, null=True)

    def __str__(self):
        return self.description
