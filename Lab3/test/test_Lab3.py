import unittest
from app.Lab3 import circle_area, trapezium_area, ellipse_area, rhombus_area

class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")

    def test_circle_area_valid(self):
        try:
            result = circle_area(3)
            self.assertAlmostEqual(result, 28.274333882308138)
            print("Test Passed: Circle area for radius 3 is correct.")
        except AssertionError:
            print("Test Failed: Circle area for radius 3 is incorrect.")
            raise

    def test_circle_area_invalid(self):
        try:
            with self.assertRaises(ValueError):
                circle_area(-1)
            print("Test Passed: Correctly raised ValueError for negative radius.")
        except AssertionError:
            print("Test Failed: Did not raise ValueError for negative radius.")
            raise

    def test_trapezium_area_valid(self):
        try:
            result = trapezium_area(3, 4, 5)
            self.assertAlmostEqual(result, 17.5)
            print("Test Passed: Trapezium area for bases 3 and 4, height 5 is correct.")
        except AssertionError:
            print("Test Failed: Trapezium area for bases 3 and 4, height 5 is incorrect.")
            raise

    def test_trapezium_area_invalid(self):
        try:
            with self.assertRaises(ValueError):
                trapezium_area('a', 4, 5)
            print("Test Passed: Correctly raised ValueError for invalid inputs.")
        except AssertionError:
            print("Test Failed: Did not raise ValueError for invalid inputs.")
            raise

    def test_ellipse_area_valid(self):
        try:
            result = ellipse_area(3, 4)
            self.assertAlmostEqual(result, 37.69911184307752)
            print("Test Passed: Ellipse area for axes 3 and 4 is correct.")
        except AssertionError:
            print("Test Failed: Ellipse area for axes 3 and 4 is incorrect.")
            raise

    def test_ellipse_area_invalid(self):
        try:
            with self.assertRaises(ValueError):
                ellipse_area('a', 4)
            print("Test Passed: Correctly raised ValueError for invalid inputs.")
        except AssertionError:
            print("Test Failed: Did not raise ValueError for invalid inputs.")
            raise

    def test_rhombus_area_valid(self):
        try:
            result = rhombus_area(3, 4)
            self.assertAlmostEqual(result, 6.0)
            print("Test Passed: Rhombus area for diagonals 3 and 4 is correct.")
        except AssertionError:
            print("Test Failed: Rhombus area for diagonals 3 and 4 is incorrect.")
            raise

    def test_rhombus_area_invalid(self):
        try:
            with self.assertRaises(ValueError):
                rhombus_area('a', 4)
            print("Test Passed: Correctly raised ValueError for invalid inputs.")
        except AssertionError:
            print("Test Failed: Did not raise ValueError for invalid inputs.")
            raise

if __name__ == "__main__":
    unittest.main()
