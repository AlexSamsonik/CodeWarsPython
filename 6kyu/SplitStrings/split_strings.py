"""
Split Strings.

Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing
second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']

"""

from re import findall


def solution(s):
    regex = "..?"
    s_list = findall(regex, s)
    if len(s) == 0:
        return []
    elif len(s) % 2 == 0:
        return s_list
    else:
        result_list = s_list[:-1]
        result_list.append(s_list[-1] + "_")
        return result_list


# The best solution
def the_best_solution(s):
    return findall(".{2}", s + "_")


# The second cool solution
def the_second_solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i + 2])
    return result
