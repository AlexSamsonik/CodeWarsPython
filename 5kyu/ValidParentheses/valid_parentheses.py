"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.
Furthermore, the input string may be empty and/or not contain any parentheses at all.
Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""


def valid_parentheses(s: str) -> bool:
    """
    The function that takes a string of parentheses, and determines if the order of the parentheses is valid.

    :param s: string variable
    :return: bool
    """

    if len(s) == 0:
        return True

    count = 0
    for i in s:
        if i == ")" and count is 0:
            return False
        if i == "(":
            count += 1
        if i == ")":
            count -= 1

    return True if count == 0 else False


# The best solution #1
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False


# The best solution #2
def valid_parentheses(string):
    count = 0
    for i in string:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0


# The best soultion #3
def valid_parentheses(string):
    string = "".join(ch for ch in string if ch in "()")
    while "()" in string: string = string.replace("()", "")
    return not string
