"""
ISBN-10 Validation.

ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9. The last digit can be 0-9 or X,
to indicate a value of 10.
An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.

For example:
ISBN     : 1 1 1 2 2 2 3 3 3  9
position : 1 2 3 4 5 6 7 8 9 10

This is a valid ISBN, because:
(1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0

Examples:
1112223339   -->  true
111222333    -->  false
1112223339X  -->  false
1234554321   -->  true
1234512345   -->  false
048665088X   -->  true
X123456788   -->  false
"""

import re


def check_that_the_first_nine_characters_are_digits(isbn: str) -> bool:
    """Check that the first nine characters are digits 0-9.

    :param isbn: ISBN-10 identifiers.
    """
    return isbn[:-1].isdigit()


def check_that_the_last_character_is_digit_or_X(isbn: str) -> bool:
    """Check that the last digit can be 0-9 or X, to indicate a value of 10.

    :param isbn: ISBN-10 identifiers.
    """
    return isbn[-1].isdigit() or isbn[-1] == "X"


def valid_ISBN10(isbn):
    """ISBN-10 Validation.

    :param isbn: ISBN-10 identifiers.
    """
    if len(isbn) == 10 and check_that_the_first_nine_characters_are_digits(isbn) \
            and check_that_the_last_character_is_digit_or_X(isbn):
        isbn_list = list(isbn)
        if isbn_list[-1] == "X":
            isbn_list = ["10" if x == "X" else x for x in list(isbn)]
        return sum([int(num1) * int(num2) for num1, num2 in zip(isbn_list, range(1, 11))]) % 11 == 0
    else:
        return False


# The best solution
def the_best_valid_ISBN10(isbn):
    return bool(re.match("\d{9}[\dX]$", isbn)) and \
           sum("0123456789X".index(d) * i for i, d in enumerate(isbn, 1)) % 11 == 0


# The second cool solution
def the_second_valid_ISBN10(isbn):
    check = re.fullmatch("[0-9]{9}X|[0-9]{10}", isbn)
    if not check:
        return False
    convert_to_int = map(lambda x: 10 if x == 'X' else int(x), isbn)

    sum_of_elements = sum([num * position for num, position in list(zip(convert_to_int, range(1, 11)))])
    return sum_of_elements % 11 == 0
