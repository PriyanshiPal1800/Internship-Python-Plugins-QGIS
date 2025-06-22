# coding=utf-8
"""Resources test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'priyakusum2000@gmail.com'
__date__ = '2023-04-22'
__copyright__ = 'Copyright 2023, Priyanshi Pal'

import unittest

from qgis.PyQt.QtGui import QIcon



class ulpin_to_latlongDialogTest(unittest.TestCase):
    """Test rerources work."""

    def setUp(self):
        """Runs before each test."""
        pass

    def tearDown(self):
        """Runs after each test."""
        pass

    def test_icon_png(self):
        """Test we can click OK."""
        path = ':/plugins/ulpin_to_latlong/icon.png'
        icon = QIcon(path)
        self.assertFalse(icon.isNull())

if __name__ == "__main__":
    suite = unittest.makeSuite(ulpin_to_latlongResourcesTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)



