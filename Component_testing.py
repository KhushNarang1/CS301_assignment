import unittest

from cultural_destination import CulturalDestination

class TestCulturalDestination(unittest.TestCase):
    def setUp(self):
        self.name = "India Cultural Hub"
        self.location = "New Delhi"
        self.heritage = "India"
        self.platform = "Digital"
        self.cultural_destination = CulturalDestination(self.name, self.location, self.heritage, self.platform)

    def test_display_info(self):
        expected_output = f"Welcome to {self.name}, located in {self.location}.\nOur cultural destination celebrates the heritage of {self.heritage} and provides a platform for emerging talents through {self.platform} technology solutions.\n"
        self.assertEqual(self.cultural_destination.display_info(), expected_output)

if __name__ == "__main__":
    unittest.main()
