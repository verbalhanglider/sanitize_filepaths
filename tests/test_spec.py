
from os.path import abspath, exists, join
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from tdfilepathsanitization.directorycreation.makers import DirectoryPathBuilder
from tdfilepathsanitization.directorycreation.utils import whitelist_approved_chars, remove_unsafe_path_traversal_commands, \
    does_the_path_exist_already, create_unextant_parents, are_the_parents_extant, create_directory

class SpecTests(TestCase):
    def setUp(self):
        self.temporary_dir = TemporaryDirectory()
    
    def tearDown(self):
        self.temporary_dir.cleanup()

    def test_whitelist_approved_chars(self):
        good_string = "/home/test/foo/bar/test/bomb"
        new_string = whitelist_approved_chars(good_string)
        self.assertEquals(good_string, new_string)

    def test_remove_unsafe_path_traversal_commands(self):
        bad_string = join("home", "test", "..", "..", "..", "var", "log")
        print(bad_string)
        new_string = remove_unsafe_path_traversal_commands(bad_string)
        self.assertEqual(new_string, join("home", "test", "var", "log"))

    def test_are_the_parents_extant(self):
        new_path = join(self.temporary_dir.name, 'fiz')
        self.assertEqual(are_the_parents_extant(new_path), new_path)

    def test_are_the_parents_extant_fails(self):
        new_path = join(self.temporary_dir.name, 'foo', 'boo')
        self.assertRaises(ValueError, are_the_parents_extant, new_path)

    def test_does_the_path_exist_already(self):
        new_path = abspath(Path(*[self.temporary_dir.name, 'foo']).as_posix())
        check = does_the_path_exist_already(new_path)
        self.assertEqual(check, False)

    def test_create_unextant_parents(self):
        new_path = abspath(Path(*[self.temporary_dir.name, 'foo', 'bar']).as_posix())
        create_unextant_parents(new_path)
        self.assertEqual(are_the_parents_extant(new_path), new_path)

    def test_create_directory(self):
        new_path = abspath(Path(*[self.temporary_dir.name, 'biz']).as_posix())
        create_directory(new_path)
        self.assertEquals(exists(new_path), True)

    def test_good_filepath_builder(self):
        new = DirectoryPathBuilder(join(self.temporary_dir.name, "test", "var", "log"))
        self.assertEqual(new.path, join(self.temporary_dir.name, "test", "var", "log"))

    def test_writing_from_filepath_builder(self):
        new = DirectoryPathBuilder(join(self.temporary_dir.name, "test", "var", "log"))
        new.write()
        self.assertEqual(exists(join(self.temporary_dir.name, "test", "var", "log")), True)

    def test_reading_filepath_builder(self):
         new = DirectoryPathBuilder(join(self.temporary_dir.name, "test", "var", "log"))
         new.write()
         contents = [x for x in new.read()]
         self.assertEqual(contents, [])
