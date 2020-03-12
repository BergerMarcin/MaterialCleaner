from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

from materialcleaner.settings import ACCESS_POLICIES

# User groups acc. ACCESS POLICIES (constance: settings.ACCESS_POLICIES):
class Command(BaseCommand):
    help = 'Step 3 @ creating new DB.\n' \
           'Populate user-groups acc.: ' + ACCESS_POLICIES
    
    def handle(self, *args, **options):
        staff = Group.objects.create(name='staff')
        regular = Group.objects.create(name='regular')
        self.stdout.write("SUCCESS! Groups created acc. ACCESS_POLICIES")
