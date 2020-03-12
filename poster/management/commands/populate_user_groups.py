from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

from materialcleaner.settings import GROUP_TYPES

# User groups acc. GROUP_TYPES ACCESS POLICIES (constance: settings.ACCESS_POLICIES):
class Command(BaseCommand):
    help = 'Step 3 @ fill-in new DB.  Populate user-groups acc. GROUP_TYPES and ACCESS_POLICIES'
    
    def handle(self, *args, **options):
        for group in GROUP_TYPES:
            Group.objects.create(name=group)
        self.stdout.write("DONE! Groups created acc. ACCESS_POLICIES")
