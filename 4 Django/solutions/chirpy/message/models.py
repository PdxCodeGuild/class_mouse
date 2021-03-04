from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Chirp(models.Model):
    message = models.CharField(max_length=280)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="chirps")
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}) {self.message[:25]}..."
