from django.core.management.base import BaseCommand, CommandError
from shortener.models import AnyzURL

class Command(BaseCommand):
    help = 'Refreshes all the AnyzURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return AnyzURL.objects.refresh_shortcodes(items=options['items'])