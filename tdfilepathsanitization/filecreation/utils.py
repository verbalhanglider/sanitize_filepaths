
from os.path import abspath, join
from PIL import Image
from pathlib import Path

from ..directorycreation.utils import are_the_parents_extant, remove_unsafe_path_traversal_commands, whitelist_approved_chars, create_unextant_parents

def make_an_image(**kwargs):
    if not kwargs.get("mode"):
        return None
    return Image.new(**kwargs)

def make_filepath(some_path_as_string):
    path_string = remove_unsafe_path_traversal_commands(some_path_as_string)
    path_string = whitelist_approved_chars(some_path_as_string) 
    path_string = abspath(some_path_as_string)
    path_string = create_unextant_parents(path_string)
    print(path_string)


