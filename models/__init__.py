#!/usr/bin/python3
""" init file to make model a package """
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
