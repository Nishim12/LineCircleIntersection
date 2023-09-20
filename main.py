import math
import unittest
import numpy as np

#The points of the line won’t be inside the circle.
#Coordinates and radiuses will be integer values.

def intersection_circle_line(point1, point2, circle_center, radius):
  # Calculate the slope of the line
  if point2[0] - point1[0] != 0:
    slope_line = (point2[1] - point1[1]) / (point2[0] - point1[0])
  
  else:
    # Handle the case when the line is vertical (undefined slope)
    # Put x-coordinate in the equation of circle to see if there is an
    # intersection of line with circle

      # Calculate the square of difference of y_cordinate of intersection and
      # y_coordinate of center of circle
        difference_y_square = radius ** 2 - (point1[0] - circle_center[0]) ** 2

        if difference_y_square < 0:
            print("No Intersection(s)")
            return "No Intersection(s)", []
        elif difference_y_square == 0:
            # One intersection point
            y_intersection = circle_center[1] + math.sqrt(difference_y_square)
            print("One Intersection(s)")
            return "One Intersection(s)", [(point1[0], y_intersection)]
        else:
            # Two intersection points
            y1 = circle_center[1] + math.sqrt(difference_y_square)
            y2 = circle_center[1] - math.sqrt(difference_y_square)
            print("Two Intersection(s)")
            return "Two Intersection(s)", [(point1[0], y1), (point1[0], y2)]
      
  # Calculate the y-intercept of the line
  y_intercept = point1[1] - slope_line * point1[0]

  # Calculate the coefficients of the quadratic equation representing the 
  # intersection of the line and the circle
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

# Assuming cylinder to be a vertical cylinder
def cylinder_line_intersection(cylinder_center, cylinder_radius, line_start, line_end):
    # Vector along the line
    line_direction = np.array(line_end) - np.array(line_start)

    # Calculate the coefficients of the quadratic equation for the intersection of the line and cylinder
    a = line_direction[0] ** 2 + line_direction[1] ** 2
    b = 2 * (line_direction[0] * (line_start[0] - cylinder_center[0]) + line_direction[1] * (line_start[1] - cylinder_center[1]))
    c = (line_start[0] - cylinder_center[0]) ** 2 + (line_start[1] - cylinder_center[1]) ** 2 - cylinder_radius ** 2

    # Calculate the discriminant
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        # No intersection
        return 0, []

    elif discriminant == 0:
        # One intersection
        t = -b / (2 * a)
        intersection_point = np.array(line_start) + t * line_direction
        return 1, [tuple(intersection_point)]

    else:
        # Two intersections
        t1 = (-b + np.sqrt(discriminant)) / (2 * a)
        t2 = (-b - np.sqrt(discriminant)) / (2 * a)
        intersection_point1 = np.array(line_start) + t1 * line_direction
        intersection_point2 = np.array(line_start) + t2 * line_direction
        return 2, [tuple(intersection_point1), tuple(intersection_point2)]

# Define a test class for intersection of circle and line
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

  def test_case_4(self):
    result, points = intersection_circle_line((5, 0), (5, 10), (0, 0), 4)
    self.assertEqual(result, "No Intersection(s)")
    self.assertEqual(points, [])
  
  def test_case_5(self):
    result, points = intersection_circle_line((2, -4), (2, 5), (0, 0), 2)
    self.assertEqual(result, "One Intersection(s)")
    self.assertAlmostEqual(points[0][0], 2.000, places=3)
    self.assertAlmostEqual(points[0][1], 0.000, places=3)

  def test_case_6(self):
    result, points = intersection_circle_line((1, -4), (1, 4), (0, 0), 2)
    self.assertEqual(result, "Two Intersection(s)")
    self.assertAlmostEqual(points[0][0], 1.000, places=3)
    self.assertAlmostEqual(points[0][1], 1.732, places=3)
    self.assertAlmostEqual(points[1][0], 1.000, places=3)
    self.assertAlmostEqual(points[1][1], -1.732, places=3)

# Defined a test class to check intersection of Cylinder and line
class TestCylinderLineIntersection(unittest.TestCase):

    def test_two_intersection(self):
        # Case where the line is outside the cylinder
        cylinder_center = (0, 0, 0)
        cylinder_radius = 2.0
        line_start = (4, 0, 0)
        line_end = (6, 0, 0)
        num_intersections,points = cylinder_line_intersection(cylinder_center, cylinder_radius, line_start, line_end)
        self.assertEqual(num_intersections, 2)
        self.assertAlmostEqual(points[0][0], 4.386, places=3)
        self.assertAlmostEqual(points[0][1], 0.000, places=3)
        self.assertAlmostEqual(points[0][2], 0.000, places=3)
        self.assertAlmostEqual(points[1][0], -6.386, places=3)
        self.assertAlmostEqual(points[1][1], 0.000, places=3)
        self.assertAlmostEqual(points[1][2], 0.000, places=3)

if __name__ == '__main__':
    unittest.main()
