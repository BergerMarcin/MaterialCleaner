from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from poster.models import SalePoster, Photo, Category
from poster.uploaded_files_operations import hash_SH1_filename
from faker import Faker
from random import randint
from datetime import datetime, timedelta

PHOTO_FILES_ROOT = 'poster/managemnt/commands/photos'

PHOTOS_NAMES = ['brick debris 1.jpg',
                'brick debris 2.jpg',
                'brick debris 3.jpg',
                'reinforced concrete debris 1.jpg',
                'reinforced concrete debris 2.jpg',
                'reinforced concrete debris 3.jpg',
                'bricks 1.jpg',
                'bricks 2.jpg',
                'bricks 3.jpg',
                'toilet seats 1.jpg',
                'toilet seats 2.jpg',
                'toilet seats 3.jpg',
                ]


class Command(BaseCommand):
    help = 'Step 7 @ fill-in new DB.  Fill-in SalePoster with Photo of model/DB'
    
    def new_photo(self, title, file_name_origin, taken_localisation):
        fake = Faker('pl_PL')
        photo = Photo()
        photo.title = title
        photo.description = fake.text()
        photo.taken_localisation = taken_localisation
        photo.taken_datetime = datetime.now() - timedelta(days=int(0, 20), hours=int(0, 6))
        photo.file_name_origin = file_name_origin
        photo.file_name_hashed = hash_SH1_filename(file_name_origin)
        
        
        return photo
    
    def handle(self, *args, **options):
        '''
        Creating SalePoster with Photos
        '''
        
        fake = Faker('pl_PL')
        categories = Category.objects.all()
        user_regulars = User.objects.filter(groups__name='regular')
        
        for category in categories:
            for index in range(1, 10):
                user = user_regulars[randint(0, len(user_regulars) - 1)]
    
                sp = SalePoster()
                sp.user = user
                sp.title = f'{category.name} {index} of {fake.name()}'
                sp.categories.add(category)
                sp.total_value = randint(-50000, 500000) / 100.0
                for _ in range(6):
                    sp.photos.add(self.new_photo(category.name, category.name + ' ' + range(1,3) + '.jpg', user.userdetail.city))
                sp.description = fake.text()
                sp.country = user.userdetail.country
                sp.city = user.userdetail.city
                sp.region = user.userdetail.region
                sp.zip_code = user.userdetail.zip_code
                sp.street = ''
                sp.active = True
                sp.save()
        
        self.stdout.write("DONE! SalePoster with Photos added to models/DB")
