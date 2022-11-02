"""
Next bigger number with the same digits

Create a function that takes a positive integer and returns the next bigger number that can be formed
by rearranging its digits.

For example:

    12 ==> 21
    513 ==> 531
    2017 ==> 2071
    nextBigger(num: 12)   // returns 21
    nextBigger(num: 513)  // returns 531
    nextBigger(num: 2017) // returns 2071

If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

    9 ==> -1
    111 ==> -1
    531 ==> -1
    nextBigger(num: 9)   // returns nil
    nextBigger(num: 111) // returns nil
    nextBigger(num: 531) // returns nil

"""


def next_bigger(number):
    s = list(str(number))
    for i in range(len(s) - 2, -1, -1):
        if s[i] < s[i + 1]:
            to_replace = s[i:]
            min_number = min([j for j in to_replace if j > to_replace[0]])
            # m = min(filter(lambda x: x > to_replace[0], to_replace))
            to_replace.remove(min_number)
            to_replace.sort()
            s[i:] = [min_number] + to_replace
            return int("".join(s))
    return -1


# The best solutions:
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s) - 2, -1, -1):
        if s[i] < s[i + 1]:
            t = s[i:]
            m = min(filter(lambda x: x > t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1


def next_bigger(n):
    # algorithm: go backwards through the digits
    # when we find one that's lower than any of those behind it,
    # replace it with the lowest digit behind that's still higher than it
    # sort the remaining ones ascending and add them to the end
    digits = list(str(n))
    for pos, d in reversed(tuple(enumerate(digits))):
        right_side = digits[pos:]
        if d < max(right_side):
            # find lowest digit to the right that's still higher than d
            first_d, first_pos = min((v, p) for p, v in enumerate(right_side) if v > d)

            del right_side[first_pos]
            digits[pos:] = [first_d] + sorted(right_side)

            return int(''.join(digits))

    return -1


def next_bigger(n):
    nums = list(str(n))
    for i in reversed(range(len(nums[:-1]))):
        for j in reversed(range(i, len(nums))):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[i + 1:] = sorted(nums[i + 1:])
                return int(''.join(nums))
    return -1


def next_bigger(n):
    i, ss = n, sorted(str(n))

    if str(n) == ''.join(sorted(str(n))[::-1]):
        return -1

    while True:
        i += 1
        if sorted(str(i)) == ss and i != n:
            return i
