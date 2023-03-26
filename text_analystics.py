import unittest

from cultural_destination import CulturalDestination

class TestCulturalDestinationTextAnalytics(unittest.TestCase):
    def test_display_info(self):
        cultural_destination = CulturalDestination("India Cultural Hub", "New Delhi", "India", "Digital")
        expected_output = "Welcome to India Cultural Hub, located in New Delhi.\nOur cultural destination celebrates the heritage of India and provides a platform for emerging talents through Digital technology solutions.\n"
        self.assertEqual(cultural_destination.display_info(), expected_output)

if __name__ == "__main__":
    unittest.main()
