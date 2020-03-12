from django.core.management.base import BaseCommand
from materialcleaner.settings import FILE_PHOTO_TYPES_BASIC

from poster.models import FileType


class Command(BaseCommand):
    help = 'Step 1 @ fill-in new DB.  Fill-in photo file types into FileType model/DB acc. FILE_PHOTO_TYPES_BASIC'
    
    def handle(self, *args, **options):
        for ft in FILE_PHOTO_TYPES_BASIC:
            FileType.objects.create(type=ft)
        
        self.stdout.write("DONE! FileType model/DB was filled with BASIC photo type files from FILE_PHOTO_TYPES_BASIC")
