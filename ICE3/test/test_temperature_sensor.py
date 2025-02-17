import unittest
from ICE3.src.temperature_sensor import temperatures_processing


class TestTemperatureProcessing(unittest.TestCase):


    def test_min_boundary(self):
        self.assertEqual(temperatures_processing([-50]), "Min: -50°C, Max: -50°C, Avg: -50.0°C")

    def test_max_boundary(self):
        self.assertEqual(temperatures_processing([150]), "Min: 150°C, Max: 150°C, Avg: 150.0°C")

    def test_near_boundaries(self):
        self.assertEqual(temperatures_processing([-49]), "Min: -49°C, Max: -49°C, Avg: -49.0°C")
        self.assertEqual(temperatures_processing([149]), "Min: 149°C, Max: 149°C, Avg: 149.0°C")


    def test_mixed_valid_invalid(self):
        self.assertEqual(temperatures_processing([-60, 20, 160]), "Out-of-bound value detected.")

    def test_alphabetic_characters(self):
        self.assertEqual(temperatures_processing([20, "abc", 30]), "Invalid input detected.")

    def test_special_characters(self):
        self.assertEqual(temperatures_processing([10, "@", -40]), "Invalid input detected.")


    def test_large_inputs(self):
        self.assertEqual(temperatures_processing([2 ** 31 - 1, -2 ** 31]), "Out-of-bound value detected.")

    def test_same_inputs(self):
        self.assertEqual(temperatures_processing([50, 50, 50]), "Min: 50°C, Max: 50°C, Avg: 50.0°C")

    def test_empty_list(self):
        self.assertEqual(temperatures_processing([]), "No input provided.")

    def test_valid_list(self):
        self.assertEqual(temperatures_processing([10, -10, 30]), "Min: -10°C, Max: 30°C, Avg: 10.0°C")










