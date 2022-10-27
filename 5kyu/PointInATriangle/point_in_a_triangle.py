"""
[Geometry B -1] Point in a triangle?

Arguments:
 - triangle is a list of three coordinate pairs on a 2D plane: e. g. [[0, 0], [5, 5], [5, 0]].
 - point is a pair of coordinates: e. g. [3, 1]

Return:
 - Return 1 for a point inside the trianle or -1 for a point outside the triangle.
 - If the point belongs to any side of the triangle, return 0.
 - If the coordinates given for the triangle are invalid, raise an exception.

Examples:
 - triangle = [[0, 0], [5, 5], [5, 0]] and point = [3, 1] return 1, because the point is inside the triangle.
 - triangle = [[0, 0], [5, 5], [5, 0]] and point = [6, 6] return -1, because the point is outside the triangle.
 - triangle = [[0, 0], [5, 5], [5, 0]] and point = [2, 0] return 0, because the point is on a side of the triangle.
 - triangle = [[0, 0], [5, 5], [2, 2]] and point = [2, 0] results in exception, because it is not a valid triangle.
"""

from math import sqrt


def point_vs_triangle(point: list, triangle: list) -> int:
    """
    Function which check is point in triangle area.

    :param point: list with point coordinates
    :param triangle: list with triangle coordinates
    :return:
        1, if the point is inside the triangle;
        -1, if the point is outside the triangle;
        0, if the point is on a side of the triangle;
        raise exception, if it is not a valid triangle.
    """

    # Point coordinates
    p1, p2 = point[0], point[1]

    # Triangle coordinates
    a1, a2 = triangle[0][0], triangle[0][1]
    b1, b2 = triangle[1][0], triangle[1][1]
    c1, c2 = triangle[2][0], triangle[2][1]

    len_ab = sqrt((b1 - a1) ** 2 + (b2 - a2) ** 2)
    len_bc = sqrt((c1 - b1) ** 2 + (c2 - b2) ** 2)
    len_ca = sqrt((a1 - c1) ** 2 + (a2 - c2) ** 2)

    if (len_ab + len_bc <= len_ca) or (len_bc + len_ca <= len_ab) or (len_ca + len_ab <= len_bc):
        raise Exception
    else:
        # Move triangle to point A(0:0)
        bx, by = b1 - a1, b2 - a2
        cx, cy = c1 - a1, c2 - a2
        px, py = p1 - a1, p2 - a2

        # After moving:
        #  pV = n * bV + m * cV, and
        #  0 <= n <= 1
        #  0 <= m <= 1
        #  n + m <= 1
        # Where, pv - P vector, bv = B vector, cV = C vector
        #
        # Solving the system of equations:
        #  px = n * bx + m * cx
        #  py = n * by + m * cy, we get
        n = (cy * px - py * cx) / (bx * cy - by * cx)
        m = (px * by - py * bx) / (by * cx - bx * cy)

        n = round(n, 9)
        m = round(m, 9)

        if (n > 0) and (n < 1) and (m > 0) and (m < 1) and (n + m < 1):
            return 1
        elif ((n == 0) and (m < 1)) or ((m == 0) and (n < 1)) or (m + n == 1):
            return 0
        else:
            return -1


# The best solution #1
def triangle_area(a, b, c):
    (xa, ya), (xb, yb), (xc, yc) = a, b, c
    return abs(xa * (yb - yc) + xb * (yc - ya) + xc * (ya - yb))


def point_vs_triangle(point, triangle):
    area = triangle_area(*triangle)
    assert area > 1e-9
    a, b, c = triangle
    pab, pbc, pca = triangle_area(point, a, b), triangle_area(point, b, c), triangle_area(point, c, a)
    if abs(pab + pbc + pca - area) > 1e-9:
        return -1
    else:
        return bool(pab > 1e-9 and pbc > 1e-9 and pca > 1e-9)
