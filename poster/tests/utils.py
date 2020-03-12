from poster.models import *
from faker import Faker
from random import randint, choice

faker = Faker("pl_PL")


def create_fake_sale_poster():
    '''
    Create new SalePoster and save to DB
    :return:
    :rtype:
    '''
    new_sale_poster = SalePoster.objects.create(
        # name=faker.word(),
        # description=faker.sentence(),
        # location=faker.address(),
        # area=randint(1, 10)
    )
    return new_sale_poster
