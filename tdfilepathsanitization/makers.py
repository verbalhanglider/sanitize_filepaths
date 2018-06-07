
from .utils import *

class FilePathBuilder:
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