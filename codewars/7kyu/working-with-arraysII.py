'''
Working with arrays II (and why your code fails in some katas)

In this kata the function returns an array/list like the one passed to it but 
with its nth element removed (with 0 <= n <= array/list.length - 1). The function
is already written for you and the basic tests pass, but random tests fail. Your
taks is to figure out why and fix it.
'''

# ORIGINAL
# def remove_nth_element(lst, n):
#     lst_copy = lst
#     del lst_copy[n]
#     return lst_copy

def remove_nth_element(lst, n):
    lst_copy = lst.copy()
    del lst_copy[n : n + 1]
    return lst_copy