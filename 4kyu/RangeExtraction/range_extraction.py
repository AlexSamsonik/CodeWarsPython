"""
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
The range includes all integers in the interval including both endpoints.
It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string
in the range format.

Example:
    solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
    # returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
"""
from itertools import groupby


def solution(args: list) -> str:
    """
    The function format list of integer.

    :param args: list of integer
    :return: format's list as string
    """

    groups = []
    for _, group in groupby(enumerate(args), key=lambda i: i[0] - i[1]):
        groups.append([g[1] for g in list(group)])

    groups_result = []
    for j in groups:
        if len(j) > 2:
            groups_result.append(f"{j[0]}-{j[-1]}")
        elif len(j) == 2:
            groups_result.append(f"{j[0]}")
            groups_result.append(f"{j[-1]}")
        else:
            groups_result.append(f"{j[0]}")

    return ",".join(groups_result)


# The best solution #1
def solution(args):
    out = []
    beg = end = args[0]

    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:
                out.append(str(beg))
            elif end == beg + 1:
                out.extend([str(beg), str(end)])
            else:
                out.append(str(beg) + "-" + str(end))
            beg = n
        end = n

    return ",".join(out)


# The best solution #2
def printable(arr):
    return (','.join(str(x) for x in arr) if len(arr) < 3  # one or two consecutive integers : comma separated
            else f'{arr[0]}-{arr[-1]}')  # more : dash separated first and last integer


def solution(args):
    chunk, ret = [], []  # instantiate variables

    for i in args:  # for each integer
        if not len(chunk) or i == chunk[-1] + 1:  # if first or consecutive
            chunk.append(i)  # add to current chunk
        else:  # else, it's a gap
            ret.append(printable(chunk))  # save current chunk
            chunk = [i]  # and restart a new one

    ret.append(printable(chunk))  # do not forget last chunk !

    return ','.join(ret)  # return comma separated chunks
