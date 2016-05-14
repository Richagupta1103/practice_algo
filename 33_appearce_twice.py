'''
I have a list where every number in the range 1...n1...n appears once except for one number which appears twice.
'''


def find_number_appear_twice(list_num):
    total = 0
    for num in list_num:
        total += num
    n = len(list_num)-1
    total_n = (n*n+n)/2
    print total - total_n


list_num = [1, 2, 4, 7, 3, 5, 6, 7, 8]
find_number_appear_twice(list_num)