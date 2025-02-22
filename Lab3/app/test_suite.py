import unittest
from test.test_Lab3 import TestShapes

def run_tests(choice):
    suite = unittest.TestSuite()

    if choice == 'c':
        suite.addTest(TestShapes('test_circle_area_valid'))
        suite.addTest(TestShapes('test_circle_area_invalid'))
    elif choice == 't':
        suite.addTest(TestShapes('test_trapezium_area_valid'))
        suite.addTest(TestShapes('test_trapezium_area_invalid'))
    elif choice == 'e':
        suite.addTest(TestShapes('test_ellipse_area_valid'))
        suite.addTest(TestShapes('test_ellipse_area_invalid'))
    elif choice == 'r':
        suite.addTest(TestShapes('test_rhombus_area_valid'))
        suite.addTest(TestShapes('test_rhombus_area_invalid'))
    else:
        print("Invalid choice. Exiting.")
        return

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    print("Please enter one of the following options:")
    print("- 'c' for testing the area of a circle")
    print("- 't' for testing the area of a trapezium")
    print("- 'e' for testing the area of an ellipse")
    print("- 'r' for testing the area of a rhombus")
    print("- 'q' to quit")
    choice = input("What would you like to do? ").strip().lower()
    if choice != 'q':
        run_tests(choice)
    else:
        print("Exiting the test suite.")
