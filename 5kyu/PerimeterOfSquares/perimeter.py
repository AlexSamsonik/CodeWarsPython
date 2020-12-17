"""
Perimeter of squares in a rectangle.

The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum
of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80.

Hint:
See Fibonacci sequence

Ref:
http://oeis.org/A000045

The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and
returns the total perimeter of all the squares.

Examples:
perimeter(5)  should return 80
perimeter(7)  should return 216
"""


def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def perimeter(n):
    return 4 * sum(list(fibonacci(n + 1)))
