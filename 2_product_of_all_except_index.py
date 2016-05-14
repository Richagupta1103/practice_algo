'''
You have a list of integers, and for each index you want
 to find the product of every integer except the integer at that index.
'''


def get_products_of_all_ints_except_at_index(int_list):

    # we make a list with the length of the input list to
    # hold our products
    products_of_all_ints_except_at_index = [None] * len(int_list)

    # for each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    i = 0
    while i < len(int_list):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]
        i += 1

    # for each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1
    i = len(int_list) - 1
    while i >= 0:
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]
        i -= 1

    return products_of_all_ints_except_at_index

int_list = [5, 3, 8, 2, 9, 6]
print get_products_of_all_ints_except_at_index(int_list)