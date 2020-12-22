"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:
 - There must be a function for each number from 0 ("zero") to 9 ("nine")
 - There must be a function for each of the following mathematical operations: plus, minus, times,
dividedBy (divided_by in Ruby and Python)
 - Each calculation consist of exactly one operation and two numbers
 - The most outer function represents the left operand, the most inner function represents the right operand
 - Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
"""


def calculate(operation=None, number=None):
    if operation[0].__name__ == "times":
        return operation[1] * number
    if operation[0].__name__ == "plus":
        return operation[1] + number
    if operation[0].__name__ == "minus":
        return number - operation[1]
    if operation[0].__name__ == "divided_by":
        return number // operation[1]
#  Numbers
def zero(operation=None): return calculate(operation, 0) if operation else 0
def one(operation=None): return calculate(operation, 1) if operation else 1
def two(operation=None): return calculate(operation, 2) if operation else 2
def three(operation=None): return calculate(operation, 3) if operation else 3
def four(operation=None): return calculate(operation, 4) if operation else 4
def five(operation=None): return calculate(operation, 5) if operation else 5
def six(operation=None): return calculate(operation, 6) if operation else 6
def seven(operation=None): return calculate(operation, 7) if operation else 7
def eight(operation=None): return calculate(operation, 8) if operation else 8
def nine(operation=None): return calculate(operation, 9) if operation else 9
# Operations
def plus(number): return plus, number
def minus(number): return minus, number
def times(number): return times, number
def divided_by(number): return divided_by, number


# The best solution
# def zero(f = None): return 0 if not f else f(0)
# def one(f = None): return 1 if not f else f(1)
# def two(f = None): return 2 if not f else f(2)
# def three(f = None): return 3 if not f else f(3)
# def four(f = None): return 4 if not f else f(4)
# def five(f = None): return 5 if not f else f(5)
# def six(f = None): return 6 if not f else f(6)
# def seven(f = None): return 7 if not f else f(7)
# def eight(f = None): return 8 if not f else f(8)
# def nine(f = None): return 9 if not f else f(9)
#
# def plus(y): return lambda x: x+y
# def minus(y): return lambda x: x-y
# def times(y): return lambda  x: x*y
# def divided_by(y): return lambda  x: x/y
