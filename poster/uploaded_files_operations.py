import datetime
import hashlib
import os

from materialcleaner.settings import MEDIA_ROOT
from .models import FileType


def hash_SH1_filename(name):
    # hashing file name with simple SHA1 to have unique name (to avoid overwriting by other user's file)
    # to original file name datetime was added just to be sure name will be unique (if 2 users give the same name than
    #   only name+datetime after hasing may result in different hashing names)
    m = hashlib.sha1()
    m.update(name.encode('utf-8') + datetime.datetime.utcnow().strftime("%H:%M:%S.%f - %b %d %Y").encode('utf-8'))
    return m.hexdigest()


def media_path_name(filename_hashed):
    return os.path.join(MEDIA_ROOT, filename_hashed)


def copy_regular_file_to_uploaded_folder(file_name_origin, path_name_origin):
    # read origin file
    filename_origin = os.path.join(path_name_origin, file_name_origin)
    if os.path.isfile(filename_origin):
        with (filename_origin, 'wb+') as file_origin:
            file_origin.read()
    else:
        return None
    
    # write file to upload folder (and hashing name)
    file_name_hashed = hash_SH1_filename(file_name_origin)
    pathname_loaded_hashed = media_path_name(file_name_hashed)
    with open(pathname_loaded_hashed, 'wb+') as file_loaded:
        for chunk in file_origin.chunks():
            file_loaded.write(chunk)
    return {'file_name_origin': file_name_origin,
            'path_name_origin': path_name_origin,
            'file_name_hashed': file_name_hashed,
            'pathname_loaded': pathname_loaded_hashed}


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
        filename_hashed = hash_SH1_filename(FILES_file.name)
        pathname_loaded_hashed = media_path_name(filename_hashed)
        with open(pathname_loaded_hashed, 'wb+') as destination:
            # to write as a chunk protect against issues with big size files
            for chunk in FILES_file.chunks():
                destination.write(chunk)
        return {'file_name_hashed': filename_hashed,
                'pathname_loaded': pathname_loaded_hashed,
                'file_type': FILES_file.content_type}
    return None
