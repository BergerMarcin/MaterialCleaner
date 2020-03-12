import pytest
from poster.models import *
from .utils import *


@pytest.mark.django_db
def test_add_sale_poster(set_up_sale_poster):
    '''
    Should create new SalePoster object and save it to database
    :param set_up_sale_poster:
    :type set_up_sale_poster:
    :return:
    :rtype:
    '''
    
    # Given:
    sale_poster_before = SalePoster.objects.count()
    
    # When:
    new_sale_poster = create_fake_sale_poster()
    
    # Then:
    assert SalePoster.objects.count() == sale_poster_before + 1
    assert SalePoster.objects.count() == 6