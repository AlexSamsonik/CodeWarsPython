"""
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account
the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

    s1 = "A aaaa bb c"
    s2 = "& aaa bbb c d"

    s1 has 4 'a', 2 'b', 1 'c'
    s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not
consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for
string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because
the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if
this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear
with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing
order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits -
more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".

Hopefully other examples can make this clearer.

    s1 = "my&friend&Paul has heavy hats! &"
    s2 = "my friend John has many many friends &"
    mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

    s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
    s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
    mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

    s1="Are the kids at home? aaaaa fffff"
    s2="Yes they are here! aaaaa fffff"
    mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
"""

import string


def count_letter(s: str) -> list[list[str]]:
    """
    Count letter in string.

    :param s: string variable or sentence
    :return: list[list[str]]
    """

    count = []
    for letter in [i for i in string.ascii_lowercase]:
        lets = list(filter(lambda x: x == letter, s))
        count.append(lets)
    return count


def filter_max_letter(count1: list[list[str]], count2: list[list[str]]):
    """
    Filter max number of letter in both list and will not consider letters when the maximum of their occurrences
    is less than or equal to 1.

    :param count1: list[list[str]]
    :param count2: list[list[str]]
    :return: max1, max2 and equal filtering lists
    """

    max1, max2, equal = [], [], []
    for i in range(26):
        if len(count1[i]) == len(count2[i]) and len(count1[i]) > 1:
            equal.append(count1[i])
        elif len(count1[i]) > len(count2[i]) and len(count1[i]) > 1:
            max1.append(count1[i])
        elif len(count1[i]) < len(count2[i]) and len(count2[i]) > 1:
            max2.append(count2[i])
    return max1, max2, equal


def create_form(max_letter: list[list[str]], separator: str) -> list[str]:
    """
    Create special form to print.

    :param max_letter: list[list[str]]
    :param separator:  string separator e.g. "1", "2" or "="
    :return: list with string format
    """
    return [f"{separator}:{item[0] * len(item)}" for item in max_letter]


def mix(s1: str, s2: str) -> str:
    """
    Substrings result, for example 2:nnnnn or 1:hhh; it contains the prefix.

    :param s1: first string
    :param s2: second string
    :return: substring result
    """

    count1 = count_letter(s1)
    count2 = count_letter(s2)

    max1, max2, equal = filter_max_letter(count1, count2)

    form1 = create_form(max1, separator="1")
    form2 = create_form(max2, separator="2")
    form_equal = create_form(equal, separator="=")

    result = form1 + form2 + form_equal
    result.sort(key=len, reverse=True)
    return '/'.join(result)


# The best solution #1
def mix(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))


# The best solution #2
def mix(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))


# The best solution #3
from collections import Counter


def mix(s1, s2):
    res = []
    c1 = Counter([c for c in s1 if c.islower()])
    c2 = Counter([c for c in s2 if c.islower()])
    for c in c1 | c2:
        if c1[c] > 1 and c1[c] > c2[c]:
            res += ['1:' + c * c1[c]]
        if c2[c] > 1 and c2[c] > c1[c]:
            res += ['2:' + c * c2[c]]
        if c1[c] > 1 and c1[c] == c2[c]:
            res += ['=:' + c * c1[c]]
    return '/'.join(sorted(res, key=lambda a: [-len(a), a]))
