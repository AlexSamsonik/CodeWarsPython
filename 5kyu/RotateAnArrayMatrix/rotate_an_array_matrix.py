"""
Write a rotate function that rotates a two-dimensional array (a matrix) either clockwise or anti-clockwise
by 90 degrees, and returns the rotated array.

The function accepts two parameters: an array, and a string specifying the direction or rotation.
The direction will be either "clockwise" or "counter-clockwise".

Here is an example of how your function will be used:

    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

rotate(matrix, "clockwise") #  Would return  [[7, 4, 1], [8, 5, 2],  [9, 6, 3]]

To help you visualize the rotated matrix, here it is formatted as a grid:

 [[7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]]

Rotated counter-clockwise it would looks like this:

 [[3, 6, 9],
  [2, 5, 8],
  [1, 4, 7]]

"""

from numpy import array, rot90


def rotate(matrix: list, direction: str) -> list:
    """
    Rotate function for two-dimensional array (a matrix) e.g.:
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

    :param matrix: two-dimensional array (a matrix)
    :param direction: clockwise or anti-clockwise by 90 degrees
    :return: the rotated array
    """

    if direction == "clockwise":
        return [list(i) for i in rot90(array(matrix), k=-1)]
    if direction == "counter-clockwise":
        return [list(i) for i in rot90(array(matrix), k=1)]


# The best solution #1
d = {"clockwise": 3, "counter-clockwise": 1}


def rotate(matrix, direction):
    return rot90(matrix, d[direction]).tolist()


# The best solution #2
def to_transposed_mat(g):
    return [*map(list, zip(*g))]


def rotate(M, direction):
    gen = reversed(M) if direction == "clockwise" else map(reversed, M)
    return to_transposed_mat(gen)


# The best solution #3
def rotate(matrix, direction):
    return [list(i)[::-1] for i in zip(*matrix)] if direction == "clockwise" \
        else [list(i) for i in reversed(list(zip(*matrix)))]
