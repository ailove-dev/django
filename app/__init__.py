# -*- coding: utf-8 -*-

from os import path, makedirs
from app.settings import CKEDITOR_UPLOAD_PATH


if not path.exists(CKEDITOR_UPLOAD_PATH):
    makedirs(CKEDITOR_UPLOAD_PATH)
