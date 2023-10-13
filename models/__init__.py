#!/usr/bin/python3
"""
Instantiates a storage object.

instantiates a file storage engine (FileStorage).
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
