import pytest
# from beehive.models import *
# from beehive.service.bee_mother_service import *
#
#
# @pytest.mark.django_db
# def test_mother_age_is_less_than_specified_time(set_up_mother):
#     """
#     Should check if mother age is less than 5 years
#     """
#
#     # Given:
#     bee_mother = BeeMother.objects.all()
#
#     # When:
#     for mother in bee_mother:
#         BeeMotherService.set_mother_age(mother)
#         BeeMotherService.set_mother_active(mother)
#
#     # Then:
#     for mother in bee_mother:
#         if mother.age_days > 1825:
#             assert mother.active == False
