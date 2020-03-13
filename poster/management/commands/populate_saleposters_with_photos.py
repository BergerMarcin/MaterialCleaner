from time import timezone

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from poster.models import SalePoster, Photo, Category, FileType
from poster.uploaded_files_operations import copy_regular_file_to_path_uploaded
from faker import Faker
from random import randint
from datetime import datetime, timedelta

PHOTO_FILES_ROOT_COMMANDS = 'poster/management/commands/photos'

PHOTOS_NAMES_COMMANDS = ['brick debris 1.jpg',
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

fake = Faker('pl_PL')


class Command(BaseCommand):
    help = 'Step 7 @ fill-in new DB.  Fill-in SalePoster with Photo of model/DB'
    
    def new_photo(self, title, file_name_origin, taken_localisation):
        photo_uploaded_data = copy_regular_file_to_path_uploaded(file_name_origin, PHOTO_FILES_ROOT_COMMANDS)
        if photo_uploaded_data is None:
            return None
        photo = Photo()
        photo.title = title
        photo.description = fake.text()
        photo.taken_localisation = taken_localisation
        photo.taken_datetime = datetime.utcnow() - timedelta(days=randint(0, 20), hours=randint(3, 8))
        photo.file_name_origin = photo_uploaded_data['file_name_origin']
        photo.file_name_hashed = photo_uploaded_data['file_name_hashed']
        photo.path_loaded = photo_uploaded_data['path_loaded']
        photo.file_type = FileType.objects.get(type='image/jpeg')
        photo.save()
        return photo
    
    def handle(self, *args, **options):
        '''
        Creating SalePoster with Photos
        '''
        
        categories = Category.objects.all()
        user_regulars = User.objects.filter(groups__name='regular')
        
        for category in categories:
            for index in range(1, 8):
                user = user_regulars[randint(0, len(user_regulars) - 1)]
                
                sp = SalePoster()
                sp.user = user
                sp.title = f'{category.name} {index} of {fake.name()}'
                sp.total_value = randint(-50000, 500000) / 100.0
                sp.description = fake.text()
                sp.country = user.userdetail.country
                sp.city = user.userdetail.city
                sp.region = user.userdetail.region
                sp.zip_code = user.userdetail.zip_code
                sp.street = ''
                sp.active = True
                sp.save()
                
                sp.categories.add(category)
                sp.save()
                
                for _ in range(4):
                    photo = self.new_photo(category.name,
                                           category.name + ' ' + str(randint(1, 3)) + '.jpg',
                                           user.userdetail.city)
                    if photo is not None:
                        sp.photos.add(photo)
                sp.save()
        
        self.stdout.write("DONE! SalePoster with Photos added to models/DB")
