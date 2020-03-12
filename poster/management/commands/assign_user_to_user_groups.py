from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand

from materialcleaner.settings import ACCESS_POLICIES


class Command(BaseCommand):
    help = 'Step 5 @ creating new DB.\n' \
           'Assign users to user-groups to define her/his permissions' + ACCESS_POLICIES
    
    def handle(self, *args, **options):
        staff = Group.objects.get(name='staff')
        regular = Group.objects.get(name='regular')
        users = User.objects.all()
        for user in users:
            if user.is_active:
                if user.is_staff:
                    user.groups.add(staff)
                if not user.is_superuser and not user.is_staff:
                    user.groups.add(regular)
                user.save()
        self.stdout.write("SUCCESS! Users assigned to groups acc. ACCESS_POLICIES")
