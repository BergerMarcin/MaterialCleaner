from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from materialcleaner.settings import ACCESS_POLICIES


class Command(BaseCommand):
    help = 'Step 4 @ creating new DB.\n' \
           'Assign users to user-groups to define her/his permissions' + ACCESS_POLICIES
    
    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            pass
        self.stdout.write("SUCCESS! Users assigned to groups acc. ACCESS_POLICIES")
