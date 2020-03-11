from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

# USERS = (
#     {'password': '1234', 'is_superuser': True, 'username': 'szef',
#      'first_name': 'Marcin', 'last_name': 'Berger', 'email': 'marcin.berger@wp.pl',
#      'is_staff': True, 'is_active': True},
#     {'password': '1234 {noop}', 'is_superuser': True, 'username': 'paprotka',
#      'first_name': 'Czesław', 'last_name': 'Paprota', 'email': 'cp@wp.pl',
#      'is_staff': True, 'is_active': True},
#     {'password': '1234', 'is_superuser': False, 'username': 'gąska',
#      'first_name': 'Mariusz', 'last_name': 'Gęgała', 'email': 'mg@wp.pl',
#      'is_staff': True, 'is_active': True},
#     {'password': '1234', 'is_superuser': False, 'username': 'konik',
#      'first_name': 'Stanisław', 'last_name': 'Pasikonik', 'email': 'sp@wp.pl',
#      'is_staff': False, 'is_active': True},
# )


class Command(BaseCommand):
    help = 'Fill-in users data into auth_user of model/DB'
    
    def handle(self, *args, **options):
        User.objects.create_superuser(password='1234', is_superuser=True, username='szef',
                                      first_name='Marcin', last_name='Berger', email='marcin.berger@wp.pl',
                                      is_staff=True, is_active=True)
        User.objects.create_superuser(password='{noop}1234', is_superuser=True, username='paprotka',
                                      first_name='Czesław', last_name='Paprota', email='cp@wp.pl',
                                      is_staff=True, is_active=True)
        User.objects.create_user(password='1234', is_superuser=False, username='gąska',
                                 first_name='Mariusz', last_name='Gęgała', email='mg@wp.pl',
                                 is_staff=True, is_active=True)
        User.objects.create_user(password='1234', is_superuser=False, username='konik',
                                 first_name='Stanisław', last_name='Pasikonik', email='sp@wp.pl',
                                 is_staff=False, is_active=True)
        self.stdout.write("SUCCESS! Users added to model/DB")
