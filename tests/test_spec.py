
from os.path import abspath
from tempfile import TemporaryDirectory
from unnittest import TestCase

from tdffilepathsanitization.utils import *

class SpecTests(TestCase):
    def setUp(self):
        pass

    def test_whitelist_approved_chars(self):
        good_string = "/home/test/foo/bar/test/bomb"
        new_string = whitelist_approve_chars(good_string)
        self.assertEquals(good_string, new_string)

    def test_remove_unsafe_path_traversal_commands(self):
        bad_string = "/home/test/../../../var/log"
        new_string = remove_unsafe_path_traversal_commands(bad_string)
        self.assertEqual(new_string, '/home/test/var/log')

    def test_are_the_parents_extant(self):
        pass

    def test_does_the_path_exist_already(self):
        t = TemporaryDirectory()
        new_path = abspath(Path(*[t.name, 'foo']).as_posix())
        
        pass

    def test_create_unextant_parents(self):
        pass

    def test_create_directory(self):

        pass