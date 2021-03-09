import json

from django.core.management.base import BaseCommand

from message.models import Chirp
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('./message/management/commands/comments.json', 'r') as file:
            raw_text = file.read()
        comments = json.loads(raw_text)

        Chirp.objects.all().delete()
        user = User.objects.get(id=1)

        for comment in comments:
            chirp = Chirp()
            chirp.message = comment['body']
            chirp.author = user
            chirp.save()
