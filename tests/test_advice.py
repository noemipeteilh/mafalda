import unittest
from advice_controller import AdviceController

class TestAdviceController(unittest.TestCase):
    def setUp(self):
        self.controller = AdviceController()

    def test_get_advice(self):
        advice = self.controller.get_advice(1)
        self.assertIsNotNone(advice)

        self.assertIn("some_expected_field", advice)

if __name__ == "__main__":
    unittest.main()
