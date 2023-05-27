import unittest
from elevation.data import elevation


class TestElevation(unittest.TestCase):

    def test_elevation(self):
        lat = 42.81827
        lon = 74.34551
        expected_elevation = 835  # replace with the expected elevation at this location

        self.assertEqual(elevation(lat, lon), expected_elevation)


if __name__ == "__main__":
    unittest.main()
