import unittest

from cultural_destination import CulturalDestination

class TestCulturalDestinationIntegration(unittest.TestCase):
    def test_cultural_destination(self):
        name = "India Cultural Hub"
        location = "New Delhi"
        heritage = "India"
        platform = "Digital"
        expected_output = f"Welcome to {name}, located in {location}.\nOur cultural destination celebrates the heritage of {heritage} and provides a platform for emerging talents through {platform} technology solutions.\n"
        cultural_destination = CulturalDestination(name, location, heritage, platform)
        self.assertEqual(cultural_destination.display_info(), expected_output)

if __name__ == "__main__":
    unittest.main()
