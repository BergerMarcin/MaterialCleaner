import datetime
import hashlib
import os

from materialcleaner.settings import MEDIA_ROOT
from .models import FileType


def is_picture_file_validated(FILES_file):
    if not FILES_file.name:
        return False
    fts = []
    for ft in FileType.objects.all():
        fts.append(ft.type)
    if not FILES_file.content_type in fts:
        return False
    return True


def hash_SH1_filename(name):
    # hashing file name with simple SHA1 to have unique name (to avoid overwriting by other user's file)
    # to original file name datetime was added just to be sure name will be unique (if 2 users give the same name than
    #   only name+datetime after hasing may result in different hashing names)
    m = hashlib.sha1()
    m.update(name.encode('utf-8') + datetime.datetime.utcnow().strftime("%H:%M:%S.%f - %b %d %Y").encode('utf-8'))
    return m.hexdigest()


def handle_uploaded_files(FILES_file):
    if is_picture_file_validated(FILES_file):
        filename_hashed = hash_SH1_filename(FILES_file.name)
        pathname = os.path.join(MEDIA_ROOT, filename_hashed)
        with open(pathname, 'wb+') as destination:
            # to write as a chunk protect against issues with big size files
            for chunk in FILES_file.chunks():
                destination.write(chunk)
        return {'file_name': filename_hashed,
                'pathname': pathname,
                'file_type': FILES_file.content_type}
    return None
