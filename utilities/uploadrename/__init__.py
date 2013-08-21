import os, uuid
from filebrowser import settings, signals


def post_upload_callback(sender, **kwargs):
    upload_dir = os.path.dirname(kwargs['file'].path)
    old_name = os.path.join(settings.MEDIA_ROOT, upload_dir, kwargs['file'].filename)
    new_name = os.path.join(settings.MEDIA_ROOT, upload_dir, str(uuid.uuid4()) + kwargs['file'].extension)
    os.rename(old_name, new_name)

signals.filebrowser_post_upload.connect(post_upload_callback)
