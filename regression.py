import unittest

from cultural_destination import CulturalDestination


class TestCulturalDestinationRegression(unittest.TestCase):
    def test_name(self):
        cultural_destination = CulturalDestination("India Cultural Hub", "New Delhi", "India", "Digital")
        self.assertEqual(cultural_destination.name, "India Cultural Hub")

    def test_location(self):
        cultural_destination = CulturalDestination("India Cultural Hub", "New Delhi", "India", "Digital")
        self.assertEqual(cultural_destination.location, "New Delhi")

    def test_heritage(self):
        cultural_destination = CulturalDestination("India Cultural Hub", "New Delhi", "India", "Digital")
        self.assertEqual(cultural_destination.heritage, "India")

    def test_platform(self):
        cultural_destination = CulturalDestination("India Cultural Hub", "New Delhi", "India", "Digital")
        self.assertEqual(cultural_destination.platform, "Digital")


if __name__ == "__main__":
    unittest.main()
