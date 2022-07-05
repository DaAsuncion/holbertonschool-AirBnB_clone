#!/usr/bin/python3
""" Unittest for FileStorage """

import models
from models.engine.file_storage import FileStorage
import unittest


class TestFile_Storage(unittest.TestCase):
    """ Unittest for FileStorage """

    def test_instances(self):
        """test with descriptive name"""
        self.assertIsInstance(save(), FileStorage)

    if __name__ == '__main__':
        unittest.main()
