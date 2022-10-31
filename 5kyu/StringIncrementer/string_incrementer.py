"""
String incrementer

Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.

Examples:
    foo -> foo1
    foobar23 -> foobar24
    foo0042 -> foo0043
    foo9 -> foo10
    foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""
from re import search


def increment_string(s: str) -> str:
    """
    Function which increments a string, to create a new string

    :param s: random string
    :return: new string with incremented digits by 1 on the end
    """
    second_part = search(r"\d+$", s)  # Digits on the end of string
    if second_part is None:
        return s + "1"
    else:
        first_part = s[:-len(second_part.group())]  # Everything before digits on the end of string
        return first_part + str(int(second_part.group()) + 1).zfill(len(second_part.group()))


# The best solution #1
def increment_string2(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng + "1"
    return head + str(int(tail) + 1).zfill(len(tail))
