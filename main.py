import math
import unittest


def intersection_circle_line(point1, point2, circle_center, radius):
  # Calculate the slope of the line
  if point2[0] - point1[0] != 0:
    slope_line = (point2[1] - point1[1]) / (point2[0] - point1[0])
  else:
    # Handle the case when the line is vertical (undefined slope)
    slope_line = float('inf')

  # Calculate the y-intercept of the line
  y_intercept = point1[1] - slope_line * point1[0]

  # Calculate the coefficients of the quadratic equation representing the intersection
  # of the line and the circle
  x_square_coefficient = 1 + slope_line**2
  x_coefficient = -2 * circle_center[0] + 2 * slope_line * (y_intercept -
                                                            circle_center[1])
  constant_term = circle_center[0]**2 + (y_intercept -
                                         circle_center[1])**2 - radius**2

  # Calculate the discriminant
  d = x_coefficient**2 - 4 * x_square_coefficient * constant_term

  if d < 0:
    print("No Intersection(s)")
    return "No Intersection(s)", []
  elif d == 0:
    x_intersection = -x_coefficient / (2 * x_square_coefficient)
    y_intersection = slope_line * x_intersection + y_intercept
    print("One Intersection(s)")
    return "One Intersection(s)", [(x_intersection, y_intersection)]
  else:
    x1 = (-x_coefficient + math.sqrt(d)) / (2 * x_square_coefficient)
    y1 = slope_line * x1 + y_intercept
    x2 = (-x_coefficient - math.sqrt(d)) / (2 * x_square_coefficient)
    y2 = slope_line * x2 + y_intercept
    print("Two Intersection(s)")
    return "Two Intersection(s)", [(x1, y1), (x2, y2)]


# Define a test class
class TestIntersectionCircleLine(unittest.TestCase):

  def test_case_1(self):
    result, points = intersection_circle_line((0, 10), (30, 10), (12, 0), 10)
    self.assertEqual(result, "One Intersection(s)")
    self.assertAlmostEqual(points[0][0], 12.0, places=3)
    self.assertAlmostEqual(points[0][1], 10.0, places=3)

  def test_case_2(self):
    result, points = intersection_circle_line((0, -10), (15, 15), (9, 3), 5)
    self.assertEqual(result, "Two Intersection(s)")
    self.assertAlmostEqual(points[0][0], 10.635, places=3)
    self.assertAlmostEqual(points[0][1], 7.725, places=3)
    self.assertAlmostEqual(points[1][0], 5.6, places=3)
    self.assertAlmostEqual(points[1][1], -0.666, places=3)

  def test_case_3(self):
    result, points = intersection_circle_line((0, -10), (15, 15), (10, -5), 4)
    self.assertEqual(result, "No Intersection(s)")
    self.assertEqual(points, [])


if __name__ == '__main__':
  unittest.main()
