'''
Write a recursive function for generating all permutations of an input string. Return them as a set.
'''


# def toString(s):
#     return ''.join(s)
#
#
# def generate_permutation(a, l, r, permutation_list):
#     if l == r:
#         permutation_list.append(toString(a))
#     else:
#         for i in range(l, r+1):
#             a[i], a[l] = a[l], a[i]
#             generate_permutation(a, l+1, r, permutation_list)
#             a[i], a[l] = a[l], a[i]
#     return permutation_list
#
# # run your function through some test cases here
# # remember: debugging is half the battle!
# permutation_list = []
# a = 'richa'
# a = list(a)
# n = len(a)
# print generate_permutation(a, 0, n-1, permutation_list)
#

def get_permutations(string):

    # base case
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    # recursive call: get all possible permutations for all chars except last
    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)

    # put the last char in all possible positions for each of the above permutations
    permutations = set()
    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = permutation_of_all_chars_except_last[:position] + last_char + permutation_of_all_chars_except_last[position:]
            permutations.add(permutation)

    return permutations
print get_permutations('rich')
