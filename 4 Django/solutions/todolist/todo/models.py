from django.db import models

# Create your models here.


class Priority(models.Model):
    name = models.CharField(max_length=10)
    order = models.IntegerField()

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    text = models.CharField(max_length=100)
    priority = models.ForeignKey(
        Priority, on_delete=models.PROTECT, related_name="todo_items")
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.text
