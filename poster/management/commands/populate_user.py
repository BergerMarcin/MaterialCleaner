from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from poster.models import UserDetail, REGIONS
from faker import Faker
from faker.providers import phone_number
from random import randint


class Command(BaseCommand):
    help = 'Step 2 @ creating new DB.  Fill-in users data into auth_user of model/DB'
    
    def fake_userdetails(self):
        fake = Faker('pl_PL')
        fake.add_provider(phone_number)
        address = fake.address()
        userdetail = UserDetail
        userdetail.phone_prim = fake.phone_number()
        userdetail.phone_second = fake.phone_number()
        userdetail.region = REGIONS[randint(0, 15)][0]
        userdetail.city = address.splitlines()[1].split(' ')[1]
        userdetail.zip_code = address.splitlines()[1].split(' ')[0]
        userdetail.street = address.splitlines()[0]
        return userdetail
    
    def handle(self, *args, **options):
        # Creating Users & UserDetail
        # u = User.objects.create_superuser(password='1234', is_superuser=True, username='szef',
        #                                   first_name='Marcin', last_name='Berger', email='marcin.berger@wp.pl',
        #                                   is_staff=True, is_active=True)
        # userdetail = self.fake_userdetails()
        # userdetail.user = u
        # userdetail.save()
        
        # u = User.objects.create_superuser(password='{noop}1234', is_superuser=True, username='paprotka',
        #                                   first_name='Czesław', last_name='Paprota', email='cp@wp.pl',
        #                                   is_staff=True, is_active=True)
        # userdetail = self.fake_userdetails()
        # userdetail.user = u
        # userdetail.save(self)
        
        u = User.objects.create_user(password='1234', is_superuser=False, username='gąska',
                                     first_name='Mariusz', last_name='Gęgała', email='mg@wp.pl',
                                     is_staff=True, is_active=True)
        userdetail = self.fake_userdetails()
        userdetail.user = u
        userdetail.save()
        
        u = User.objects.create_user(password='1234', is_superuser=False, username='konik',
                                     first_name='Stanisław', last_name='Pasikonik', email='sp@wp.pl',
                                     is_staff=False, is_active=True)
        userdetail = self.fake_userdetails()
        userdetail.user = u
        userdetail.save()
        
        self.stdout.write("SUCCESS! Users added to model/DB")
