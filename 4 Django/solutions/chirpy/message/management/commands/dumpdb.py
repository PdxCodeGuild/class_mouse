from django.core.management.base import BaseCommand

from message.models import Chirp


class Command(BaseCommand):

    def handle(self, *args, **options):
        Chirp.objects.all().delete()
