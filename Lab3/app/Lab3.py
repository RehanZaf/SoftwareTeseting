'''
Name: Rehan Zaffar
Date: Feb 21st, 2025
Description: This program runs test cases with functions that calculate areas of a circle, trapezium, ellipse, rhombus.
'''
from math import pi

def circle_area(r):
    if isinstance(r, (int, float)) and r >= 0:
        return pi * (r ** 2)
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")

def trapezium_area(a, b, h):
    if all(isinstance(val, (int, float)) and val > 0 for val in [a, b, h]):
        return 0.5 * (a + b) * h
    else:
        raise ValueError("Invalid inputs. All inputs must be positive numbers.")

def ellipse_area(a, b):
    if all(isinstance(val, (int, float)) and val > 0 for val in [a, b]):
        return pi * a * b
    else:
        raise ValueError("Invalid inputs. Both inputs must be positive numbers.")

def rhombus_area(d1, d2):
    if all(isinstance(val, (int, float)) and val > 0 for val in [d1, d2]):
        return 0.5 * d1 * d2
    else:
        raise ValueError("Invalid inputs. Both inputs must be positive numbers.")

