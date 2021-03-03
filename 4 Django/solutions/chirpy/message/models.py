from django.db import models

# Create your models here.


class Chirp(models.Model):
    message = models.CharField(max_length=280)
    author = models.CharField(max_length=20)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}) {self.message[:25]}..."
