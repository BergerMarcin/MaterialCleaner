from django.core.management.base import BaseCommand

from .populate_file_types import Command as Populate_file_types
from .populate_users_with_userdetails import Command as Populate_users_with_userdetails
from .populate_user_groups import Command as Populate_user_groups
from .assign_permissions_to_user_groups import Command as Assign_permissions_to_user_groups
from .assign_user_to_user_groups import Command as Assign_user_to_user_groups
from .populate_categories import Command as Populate_categories
from .populate_saleposters_with_photos import Command as Populate_saleposters_with_photos

prepare_DB_commands_classes = [
    Populate_file_types(),
    Populate_users_with_userdetails(),
    Populate_user_groups(),
    Assign_permissions_to_user_groups(),
    Assign_user_to_user_groups(),
    Populate_categories(),
    Populate_saleposters_with_photos(),
]


class Command(BaseCommand):
    help = 'Fill-in new, clear DB (after drop and migrate) using all single methods for fill-in'

    def handle(self, *args, **options):
        for i, prep in enumerate(prepare_DB_commands_classes):
            print(f'STEP {i}')
            print(prep.help)
            prep.handle()
            print()
        print('DONE! FINISHED! PLS CHECK DB!')
