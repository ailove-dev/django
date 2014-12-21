# -*- coding: utf-8 -*-

from os import path, makedirs
from app.settings import CKEDITOR_UPLOAD_PATH

# uncomment if use PyMySQL
# try:
#     from pymysql import install_as_MySQLdb
#     install_as_MySQLdb()
# except ImportError:
#     pass

if not path.exists(CKEDITOR_UPLOAD_PATH):
    makedirs(CKEDITOR_UPLOAD_PATH)
