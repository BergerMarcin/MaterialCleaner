import string

from django.contrib.auth.models import Group
from materialcleaner.settings import GROUP_TYPES, FILE_PHOTO_TYPES_BASIC, CATEGORIES_BASIC, REGIONS

from poster.models import *
from faker import Faker
from faker.providers import phone_number
from random import randint
from poster.management.commands.populate_saleposters_with_photos import Command as PopulateSalepostersWithPhotosCommand
from poster.management.commands.populate_saleposters_with_photos import PHOTOS_NAMES_COMMANDS

fake = Faker("pl_PL")
fake.add_provider(phone_number)


# Function to count objects (and avoid exception)
def model_count(classmodel):
    try:
        return classmodel.objects.count()
    except classmodel.DoesNotExist:
        return 0


# --------------------------------
# Fake Group creation part (functions be applied if ONLY ONCE CALLED - to avoid double groups)

def create_fake_group():
    new_group_name = GROUP_TYPES[randint(0, len(GROUP_TYPES) - 1)]
    new_group = Group.objects.create(name=new_group_name)
    return new_group


# --------------------------------
# Fake User creation part

def create_group_assign_user_to_group(new_user, group_name):
    group = Group.objects.get(name=group_name)
    if not group:
        group = Group.objects.create(name=group_name)
    new_user.groups.add(group)
    new_user.save()
    return new_user


def create_fake_user_acc_params(is_superuser, group, is_active):
    password = str(fake.text()[:6].replace(string.whitespace, ''))
    u_name = fake.name().split(' ').pop()
    # while ((model_count(User) > 1) and (User.objects.get(username=u_name) is not None)):
    #     u_name = fake.name().split(' ').pop()
    username = u_name
    name = fake.name().split(' ')
    first_name = name[0]
    last_name = name.pop()
    email = fake.email()
    if is_superuser:
        new_user = User.objects.create_superuser(password=password, is_superuser=True, username=username,
                                                 first_name=first_name, last_name=last_name, email=email,
                                                 is_staff=True, is_active=is_active)
        new_user = create_group_assign_user_to_group(new_user, 'staff')
    elif group == 'staff':
        new_user = User.objects.create_user(password=password, is_superuser=False, username=username,
                                            first_name=first_name, last_name=last_name, email=email,
                                            is_staff=True, is_active=is_active)
        new_user = create_group_assign_user_to_group(new_user, 'staff')
    elif group == 'regular':
        new_user = User.objects.create_user(password=password, is_superuser=False, username=username,
                                            first_name=first_name, last_name=last_name, email=email,
                                            is_staff=False, is_active=is_active)
        new_user = create_group_assign_user_to_group(new_user, 'regular')
    return new_user


def create_fake_user_superuser():
    new_user = create_fake_user_acc_params(True, 'staff', True)
    return new_user


def create_fake_user_staff():
    new_user = create_fake_user_acc_params(False, 'staff', True)
    return new_user


def create_fake_user_regular():
    new_user = create_fake_user_acc_params(False, 'regular', True)
    return new_user


# --------------------------------
# Fake User with UserDetail creation part

def create_fake_user_regular_with_user_details():
    new_user = create_fake_user_regular()
    address = fake.address()
    
    new_user_detail = UserDetail()
    new_user_detail.phone_prim = fake.phone_number()
    new_user_detail.phone_second = fake.phone_number()
    new_user_detail.region = REGIONS[randint(0, 15)][0]
    new_user_detail.city = address.splitlines()[1].split(' ')[1]
    new_user_detail.zip_code = address.splitlines()[1].split(' ')[0]
    new_user_detail.street = address.splitlines()[0]
    new_user_detail.user = new_user
    new_user_detail.save()
    
    return new_user


# --------------------------------
# Fake FileType creation part

def create_fake_file_type():
    new_file_type_name = FILE_PHOTO_TYPES_BASIC[randint(0, len(FILE_PHOTO_TYPES_BASIC) - 1)]
    new_file_type = FileType.objects.create(type=new_file_type_name)
    return new_file_type


# --------------------------------
# Fake Category creation part

def create_fake_category():
    new_category_name = CATEGORIES_BASIC[randint(0, len(CATEGORIES_BASIC) - 1)]
    new_category = Category.objects.create(name=new_category_name['en'])
    return new_category


# --------------------------------
# Fake Photo creation part (file names acc. PHOTOS_NAMES_COMMANDS, only *.jpg)

def create_fake_photo():
    pspwpc = PopulateSalepostersWithPhotosCommand()
    if not FileType.objects.filter(type='image/jpeg'):
        FileType.objects.create(type='image/jpeg')
    new_photo = pspwpc.new_photo(CATEGORIES_BASIC[randint(0, len(CATEGORIES_BASIC) - 1)]['en'],
                                 PHOTOS_NAMES_COMMANDS[randint(0, len(PHOTOS_NAMES_COMMANDS) - 1)],
                                 fake.address().splitlines()[1].split(' ')[1])
    return new_photo


# --------------------------------
# Fake SalePoster creation part

def create_fake_sale_poster_with_user_userdetail_category_photos():
    '''
    Creating new SalePoster(fake = random)
    AS WELL AS creating:
     - Group(name='regular') - exactly 1pcs.
     - User(fake but belongs to regular group)  &  UserDetail(fake = random) - 1pcs./class
     - Category(fake = random) - 1pcs.
     - Photos(file names acc. PHOTOS_NAMES_COMMANDS, only *.jpg) - 4pcs.
    and save them to DB
    :return:
    :rtype: 1 SalePoster object saved
    '''
    user = create_fake_user_regular_with_user_details()
    category = create_fake_category()
    
    new_sale_poster = SalePoster()
    new_sale_poster.user = user
    new_sale_poster.title = f'{category.name} {randint(1, 8)} of {fake.name()}'
    new_sale_poster.total_value = randint(-50000, 500000) / 100.0
    new_sale_poster.description = fake.text()
    new_sale_poster.country = user.userdetail.country
    new_sale_poster.city = user.userdetail.city
    new_sale_poster.region = user.userdetail.region
    new_sale_poster.zip_code = user.userdetail.zip_code
    new_sale_poster.street = user.userdetail.street
    new_sale_poster.active = True
    new_sale_poster.save()
    
    new_sale_poster.categories.add(category)
    new_sale_poster.save()
    
    # create photos and assign to new_sale_poster
    pspwpc = PopulateSalepostersWithPhotosCommand()
    for _ in range(4):
        photo = pspwpc.new_photo(category.name,
                                 category.name + ' ' + str(randint(1, 3)) + '.jpg',
                                 user.userdetail.city)
        if photo is not None:
            new_sale_poster.photos.add(photo)
    new_sale_poster.save()
    
    return new_sale_poster
