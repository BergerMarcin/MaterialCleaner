from django.core.management.base import BaseCommand
from materialcleaner.settings import CATEGORIES_BASIC

from poster.models import Category


class Command(BaseCommand):
    help = 'Step 6 @ fill-in new DB.  Fill-in poster categories into Categories model/DB acc. CATEGORIES_BASIC'
    
    def handle(self, *args, **options):
        for cat in CATEGORIES_BASIC:
            Category.objects.create(name=cat['en'])
        
        self.stdout.write("DONE! Categories model/DB was filled with BASIC poster categories from CATEGORIES_BASIC")
