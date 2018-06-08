
from os.path import abspath, basename, dirname, join
from PIL import Image
from pathlib import Path
from xml.etree.ElementTree import ElementTree, Element, SubElement

from ..directorycreation.utils import are_the_parents_extant, remove_unsafe_path_traversal_commands, whitelist_approved_chars, create_unextant_parents

def make_an_image(**kwargs):
    if not kwargs.get("mode"):
        return None
    return Image.new(**kwargs)

def make_filepath(some_path_as_string):
    basen = basename(some_path_as_string)
    directories = dirname(some_path_as_string)
    dir_path_string = remove_unsafe_path_traversal_commands(directories)
    dir_path_string = whitelist_approved_chars(directories)
    path_string = abspath(join(dir_path_string, basen))
    path_string = create_unextant_parents(path_string)
    return path_string

def make_a_pdf(some_path_as_string, height=860, width=400):
    path = make_filepath(some_path_as_string)
    new_image = make_an_image(**{"mode": "L", "size": (height, width)})
    new_image.save(path, 'PDF', resolution=100.0)
    return path

def make_a_jpeg(some_path_as_string, height=500, width=500):
    path = make_filepath(some_path_as_string)
    new_image = make_an_image(**{"mode": "L", "size": (height, width)})
    new_image.save(path, 'JPEG', resolution=100.0)
    return path

def make_an_xml_file(some_path_as_string):
    path = make_filepath(some_path_as_string)
    xml_element = Element("root")
    subel = SubElement(xml_element, "test")
    subel.text = "testing..." 
    tree = ElementTree(xml_element)
    tree.write(path, xml_declaration=True, encoding="utf-8")


def make_a_text_file(some_path_as_string):
    path = make_filepath(some_path_as_string)
    with open(path, 'w+', encoding="utf-8") as write_file:
        write_file.write("this is a test file...")
    