def find_palindrom_permutation(s):
    dict_char = {}
    for i in range(len(s)):
        if s[i] in dict_char:
            dict_char[s[i]] += 1
        else:
            dict_char[s[i]] = 1
    count = 0
    for key,value in dict_char.iteritems():
        if value % 2 != 0 and count > 0:
            return False
        elif value % 2 != 0:
            count += 1
    return True


print find_palindrom_permutation('ririrrri')