import os
import sys
import pytest
from .utils import *


# sys.path.append(os.path.dirname(__file__))

@pytest.fixture
def set_up_sale_poster():
    data = []
    for _ in range(5):
        data_object = create_fake_sale_poster()
        data.append(data_object)
    return data
