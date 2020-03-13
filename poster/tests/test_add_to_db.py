import pytest
from django.db.models import Q

from .utils import *


@pytest.mark.django_db
def test_add_group(set_up_group):
    '''
    Should create new Group objects and save them to DB
    '''
    
    # Given:
    model_count_before = Group.objects.count()
    
    # When:
    pass
    
    # Then:
    assert Group.objects.count() == model_count_before
    assert Group.objects.count() == len(GROUP_TYPES)
    assert Group.objects.filter(name=GROUP_TYPES[0]).count() == 1
    assert Group.objects.filter(name=GROUP_TYPES[1]).count() == 1


@pytest.mark.django_db
def test_add_user(set_up_group, set_up_user):
    '''
    Should create new User objects and save them to DB
    '''
    
    # Given:
    model_count_before = User.objects.count()
    
    # When:
    new_model_object = create_fake_user_superuser()
    
    # Then:
    assert User.objects.count() == model_count_before + 1
    assert User.objects.count() == 4
    assert User.objects.filter(is_superuser=True).count() == 2
    assert User.objects.filter(groups__name='staff').count() == 3
    assert User.objects.filter(groups__name='regular').count() == 1


@pytest.mark.django_db
def test_add_user_regular_with_user_detail(set_up_group, set_up_user_regular_with_user_detail):
    '''
    Should create new regular User with UserDetail objects and save them to DB
    '''
    
    # Given:
    model_count_before = User.objects.count()
    
    # When:
    new_model_object = create_fake_user_superuser()
    
    # Then:
    assert User.objects.count() == model_count_before + 1
    assert User.objects.count() == 4
    assert User.objects.filter(is_superuser=True).count() == 1
    assert User.objects.filter(groups__name='staff').count() == 1
    assert User.objects.filter(groups__name='regular').count() == 3
    assert len(User.objects.filter(groups__name='regular')[0].email) > 0
    assert len(User.objects.filter(groups__name='regular')[1].userdetail.phone_prim) > 0
    assert len(User.objects.filter(groups__name='regular')[2].userdetail.city) > 0


@pytest.mark.django_db
def test_add_file_type(set_up_file_type):
    '''
    Should create new FileType objects and save them to DB
    '''
    
    # Given:
    model_count_before = FileType.objects.count()
    
    # When:
    new_model_object = create_fake_file_type()
    
    # Then:
    assert FileType.objects.count() == model_count_before + 1
    assert FileType.objects.count() == 4


@pytest.mark.django_db
def test_add_category(set_up_category):
    '''
    Should create new Category objects and save them to DB
    '''
    
    # Given:
    model_count_before = Category.objects.count()
    
    # When:
    new_model_object = create_fake_category()
    
    # Then:
    assert Category.objects.count() == model_count_before + 1
    assert Category.objects.count() == 4


@pytest.mark.django_db
def test_add_photo(set_up_photo):
    '''
    Should create new Photo objects and save them to DB
    '''
    
    # Given:
    model_count_before = Photo.objects.count()
    
    # When:
    new_model_object = create_fake_photo()
    
    # Then:
    assert Photo.objects.count() == model_count_before + 1
    assert Photo.objects.count() == 7


@pytest.mark.django_db
def test_add_sale_poster_with_user_userdetail_category_photos(
        set_up_group,
        set_up_sale_poster_with_user_userdetail_category_photos):
    '''
    Should create new SalePoster objects and save them to DB
    '''
    
    # Given:
    model_count_before = SalePoster.objects.count()
    
    # When:
    new_model_object = create_fake_sale_poster_with_user_userdetail_category_photos()
    
    # Then:
    assert SalePoster.objects.count() == model_count_before + 1
    assert SalePoster.objects.count() == 5
    assert Group.objects.count() == 2
    assert User.objects.count() == 5
    assert User.objects.filter(groups__name='regular').count() == 5
    assert UserDetail.objects.count() == 5
    assert Category.objects.count() == 5
    assert Photo.objects.count() == (5 * 4)
