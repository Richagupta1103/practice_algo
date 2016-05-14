def bracket_validator(s):
    s=list(s)
    brackets_list = []
    l=len(s)
    i=0
    while i < l:
        if s[i] == '[' or s[i] == '{' or s[i] == '(':
            brackets_list.append(s[i])
        elif s[i] == ']':
            a = brackets_list.pop()
            if a != '[':
                return False
        elif s[i] == ')':
            a = brackets_list.pop()
            if a != '(':
                return False
        elif s[i] == '}':
            a = brackets_list.pop()
            if a != '{':
                return False
        i += 1
    if not brackets_list:
        return True
    else:
        return False

print bracket_validator('{([])}(){}{}{}')