from django.core.management.base import BaseCommand

from poster.models import FileType

FILE_TYPE = (
    ('image/jpeg'),
    ('image/bmp'),
    ('image/gif'),
    ('image/png'),
    ('image/tiff'),
    ('image/webp'),
)


class Command(BaseCommand):
    help = 'Step 1 @ creating new DB.  Fill-in picture file types into FileType model/DB'
    
    def handle(self, *args, **options):
        for ft in FILE_TYPE:
            FileType.objects.create(type=ft)
        
        self.stdout.write(f"SUCCESS! FileType model/DB was filled with picture type files from {FILE_TYPE}")
