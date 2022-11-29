#!/usr/bin/bash/python3
""" Creating a unique storage instance."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
