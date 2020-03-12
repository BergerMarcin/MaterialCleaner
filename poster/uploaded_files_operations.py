import datetime
import hashlib
import os
import shutil

from materialcleaner.settings import MEDIA_ROOT
from .models import FileType


def hash_SH1_file_name(file_name):
    # hashing file name with simple SHA1 to have unique name (to avoid overwriting by other user's file)
    # to original file name datetime was added just to be sure name will be unique (if 2 users give the same name than
    #   only name+datetime after hasing may result in different hashing names)
    m = hashlib.sha1()
    m.update(file_name.encode('utf-8') + datetime.datetime.utcnow().strftime("%H:%M:%S.%f - %b %d %Y").encode('utf-8'))
    return m.hexdigest()


def copy_regular_file_to_path_uploaded(file_name_origin, path_name_origin):
    # read origin file
    filename_origin = os.path.join(path_name_origin, file_name_origin)
    file_name_hashed = hash_SH1_file_name(file_name_origin)
    filename_loaded_hashed = os.path.join(MEDIA_ROOT, file_name_hashed)
    if os.path.isfile(filename_origin) or os.path.isfile(filename_loaded_hashed):
        shutil.copyfile(filename_origin, filename_loaded_hashed)
        return {'file_name_origin': file_name_origin,
                'path_name_origin': path_name_origin,
                'file_name_hashed': file_name_hashed,
                'path_loaded': MEDIA_ROOT}
    return None


def is_uploaded_photo_file_valid(FILES_file):
    if not FILES_file.name:
        return False
    fts = []
    for ft in FileType.objects.all():
        fts.append(ft.type)
    if not FILES_file.content_type in fts:
        return False
    return True


def handle_uploaded_photo_files(FILES_file):
    if is_uploaded_photo_file_valid(FILES_file):
        file_name_hashed = hash_SH1_file_name(FILES_file.name)
        filename_loaded_hashed = os.path.join(MEDIA_ROOT, file_name_hashed)
        with open(filename_loaded_hashed, 'wb+') as destination:
            # to write as a chunk protect against issues with big size files
            for chunk in FILES_file.chunks():
                destination.write(chunk)
        return {'file_name_hashed': file_name_hashed,
                'path_loaded': MEDIA_ROOT,
                'file_type': FILES_file.content_type}
    return None
