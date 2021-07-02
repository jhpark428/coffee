import unittest

class AssertionTest(unittest.TestCase):

    def test_with_places(self):
        first = 3.1415
        second = 3.1416
        places = 4

        self.assertAlmostEqual(first, second, places=places)

    def test_with_delta(self):
        first = 3.1415
        second = 3.1416
        delta = .005

        self.assertAlmostEqual(first, second, delta=delta)

