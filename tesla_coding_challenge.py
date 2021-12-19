"""
Given two 2D polygons write a function that calculates the IoU of their areas,
defined as the area of their intersection divided by the area of their union.
The vertices of the polygons are constrained to lie on the unit circle and you
can assume that each polygon has at least 3 vertices, given and in sorted order.

- You are free to use basic math functions/libraries (sin, cos, atan2, numpy etc)
  but not geometry-specific libraries (such as shapely).
- You are free to look up geometry-related formulas, optionally copy paste in
  short code snippets and adapt them to your needs.
- We do care and evaluate your general code quality, structure and readability
  but you do not have to go crazy on docstrings.
"""

""" 
some general sources since I did rely on code from Stack Overflow:
https://stackoverflow.com/questions/24467972/calculate-area-of-polygon-given-x-y-coordinates
https://stackoverflow.com/questions/3252194/numpy-and-line-intersections
"""

import numpy as np
from math import atan2

def iou(poly1, poly2):
    # interesection / union 
    if (poly1 == poly2):
        return 1
    intersection = calculate_intersection_area(poly1, poly2)
    union = calculate_union_area(poly1, poly2, intersection)
    return intersection / union # your code here

def poly_area(polygon):
    # returns area calculated by shoelace formula
    area = 0.0
    for i in range(len(polygon)):
        j = (i + 1) % len(polygon)
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    area = abs(area) / 2.0
    return area


def poi (a1,a2,b1,b2):
    # returns point of intersection for two lines (4 points)
    s = np.vstack([a1,a2,b1,b2])        
    h = np.hstack((s, np.ones((4, 1))))
    l1 = np.cross(h[0], h[1]) 
    l2 = np.cross(h[2], h[3]) 
    x, y, z = np.cross(l1, l2)
    if z == 0:  # lines are parallel
        return (float('inf'), float('inf'))
    return (x/z, y/z)

def find_pois(poly1, poly2):
    # find all points of intersection for two polygons
    # return a list of points of intersection, basically a new polygon
    polygon_poi = []
    orientations = []
    
    # check for intersection between all combinations of lines
    for i in range(-1,len(poly1)-1):
        for j in range(-1,len(poly2)-1):
            point = poi(poly1[i], poly1[i+1], poly2[j], poly2[j+1])
            if (within_circle(point)):
                polygon_poi.append(point)
                orientations.append(atan2(point[1], point[0]))
    
    # sort based on orientation to get appropriate area
    polygon_poi = list(dict.fromkeys(polygon_poi))
    sorted_polygon = [x for _, x in sorted(zip(orientations, polygon_poi))]
    return sorted_polygon

def within_circle(point):
    # check if point is within circle
    d = np.sqrt(point[0]**2 + point[1]**2)
    return d < 1

def calculate_intersection_area(poly1, poly2):
    # calculate intersecting area of two polygons
    intersection_polygon = find_pois(poly1, poly2)
    intersection_area = poly_area(intersection_polygon)
    return intersection_area

def calculate_union_area(poly1, poly2, intersection):
    # calculate union area of two polygons
    return poly_area(poly1) + poly_area(poly2) - intersection

# --------------------------------------------------------

if __name__ == "__main__":

    cases = []
    # Case 1: a vanilla case (see https://imgur.com/a/dSKXHPF for a diagram)
    poly1 = [
        (-0.7071067811865475, 0.7071067811865476),
        (0.30901699437494723, -0.9510565162951536),
        (0.5877852522924729, -0.8090169943749476),
    ]
    poly2 = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
        (0.7071067811865475, -0.7071067811865477),
    ]
    cases.append((poly1, poly2, "simple case", 0.12421351279682288))
    # Case 2: another simple case
    poly1 = [
        (1, 0),
        (0, 1),
        (-0.7071067811865476, -0.7071067811865476),
    ]
    poly2 = [
        (-0.1736481776669303, 0.984807753012208),
        (-1, 0),
        (0, -1),
    ]
    cases.append((poly1, poly2, "simple case 2", 0.1881047657147776))
    # Case 3: yet another simple case, note the duplicated point
    poly1 = [
        (0, -1),
        (-1, 0),
        (-1, 0),
        (0, 1),
    ]
    poly2 = [
        (0.7071067811865476, 0.7071067811865476),
        (-0.7071067811865476, 0.7071067811865476),
        (-0.7071067811865476, -0.7071067811865476),
        (0.7071067811865476, -0.7071067811865476),
        (0.7071067811865476, -0.7071067811865476),
    ]
    cases.append((poly1, poly2, "simple case 3", 0.38148713966109243))

    # Case 4: shared edge
    poly1 = [
        (-1, 0),
        (-0.7071067811865476, -0.7071067811865476),
        (0.7071067811865476, -0.7071067811865476),
        (1, 0),
    ]
    poly2 = [
        (0, 1),
        (-1, 0),
        (1, 0),
    ]
    cases.append((poly1, poly2, "shared edge", 0.0))

    # Case 5: same polygon
    poly1 = [
        (0, -1),
        (-1, 0),
        (1, 0),
    ]
    poly2 = [
        (0, -1),
        (-1, 0),
        (1, 0),
    ]
    cases.append((poly1, poly2, "same same", 1.0))

    # Case 6: polygons do not intersect
    poly1 = [
        (-0.7071067811865476, 0.7071067811865476),
        (-1, 0),
        (-0.7071067811865476, -0.7071067811865476),
    ]
    poly2 = [
        (0.7071067811865476, 0.7071067811865476),
        (1, 0),
        (0.7071067811865476, -0.7071067811865476),
    ]
    cases.append((poly1, poly2, "no intersection", 0.0))


    import time
    t0 = time.time()

    for poly1, poly2, description, expected in cases:
        computed = iou(poly1, poly2)
        print('-'*20)
        print(description)
        print("computed:", computed)
        print("expected:", expected)
        print("PASS" if abs(computed - expected) < 1e-8 else "FAIL")

    # details here don't matter too much, but this shouldn't be seconds
    dt = (time.time() - t0) * 1000
    print("done in %.4fms" % dt)
