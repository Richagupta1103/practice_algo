'''


I like parentheticals (a lot).

"Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

Write a function that, given a sentence like the one above, along with the position of
an opening parenthesis, finds the corresponding closing parenthesis.

Example: if the example string above is input with the number 10 (position of the first parenthesis),
the output should be 79 (position of the last parenthesis).

'''

def give_matching_paren(string, pos):

    length = len(string)
    count = 1
    for i in range(pos+1,length):
        if not count:
            return i-1
        if string[i] == '(':
            count += 1
        elif string[i] == ')':
            count -= 1
        i += 1
    return False

s = "Sometimes (wwwwhen I nest them (my parentheticals)()()() too much (like this (and this))) they get confusing."
print give_matching_paren(s,10)
