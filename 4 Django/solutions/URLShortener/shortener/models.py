from django.db import models

# Create your models here.


class ShortenedURL(models.Model):
    code = models.CharField(max_length=5, unique=True)
    url = models.URLField(unique=True)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.code} -- {self.url}"
