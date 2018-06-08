
from io import BytesIO
from os import scandir
from sys import getsizeof

from .utils import create_directory, create_unextant_parents, remove_unsafe_path_traversal_commands, whitelist_approved_chars
from ..constants import VALID_MIMETYPES

class DirectoryPathBuilder:
    def __init__(self, some_path):
        self.path = self._clean_path(some_path)

    def _clean_path(self, some_string):
        some_string = remove_unsafe_path_traversal_commands(some_string)  
        some_string = whitelist_approved_chars(some_string)
        return some_string

    def write(self):
        some_string = create_unextant_parents(self.path)
        some_string = create_directory(self.path)
        return some_string

    def read(self, path=None):
        if path:
            potentials = scandir(path)
        else:
            potentials = scandir(self.path)
        for n in potentials:
            if n.isdir():
                yield from self.read(path=n.path)
            elif n.isfile():
                yield n.path

    def add_file(self, mimetype=None, binary_data=None):
        file_creator = VALID_MIMETYPES.get(mimetype)
        if mimetype in VALID_MIMETYPES:
            
            pass
        return "hi"