from itertools import chain, count, islice

def digit_finder(n):
    import pdb;pdb.set_trace()
    digits = chain.from_iterable(str(i) for i in count(1))
    return int(next(islice(digits, n - 1, None)))

print(digit_finder(100))