import os
import sys
import pytest
from .utils import *


# sys.path.append(os.path.dirname(__file__))

@pytest.fixture
def set_up_group():
    model_objects = []
    for _ in range(2):
        model_object = create_fake_group()
        model_objects.append(model_object)
    return model_objects


@pytest.fixture
def set_up_user():
    model_objects = []
    model_objects.append(create_fake_user_superuser())
    model_objects.append(create_fake_user_staff())
    model_objects.append(create_fake_user_regular())
    return model_objects


@pytest.fixture
def set_up_user_detail():
    model_objects = []
    for _ in range(3):
        model_object = create_fake_user_detail()
        model_objects.append(model_object)
    return model_objects


@pytest.fixture
def set_up_user_with_user_detail():
    model_objects = []
    model_objects.append(create_fake_user_superuser())
    model_objects.append(create_fake_user_staff())
    model_objects.append(create_fake_user_regular())
    for user in model_objects:
        new_user_detail = create_fake_user_detail()
        new_user_detail.user = user
        new_user_detail.save()
    return model_objects


@pytest.fixture
def set_up_file_type():
    model_objects = []
    for _ in range(3):
        model_object = create_fake_file_type()
        model_objects.append(model_object)
    return model_objects


@pytest.fixture
def set_up_category():
    model_objects = []
    for _ in range(3):
        model_object = create_fake_category()
        model_objects.append(model_object)
    return model_objects


@pytest.fixture
def set_up_photo():
    model_objects = []
    for _ in range(4):
        model_object = create_fake_photo()
        model_objects.append(model_object)
    return model_objects


@pytest.fixture
def set_up_sale_poster_with_user_userdetail_category_photos():
    model_objects = []
    for _ in range(4):
        model_object = create_fake_sale_poster_with_user_userdetail_category_photos()
        model_objects.append(model_object)
    return model_objects
