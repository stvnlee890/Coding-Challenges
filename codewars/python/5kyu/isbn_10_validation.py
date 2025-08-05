# ISBN 10 Validation

# ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9. 
# The last digit can be 0-9 or X, to indicate a value of 10.
# An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.
# 
# For example:
# 
# ISBN     : 1 1 1 2 2 2 3 3 3 9
# position : 1 2 3 4 5 6 7 8 9 10
#
# This is a valid ISBN, because:
# 
# (1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0

# PASSED but need to refactor
def valid_ISBN10(isbn): 
    if len(isbn) != 10: return False

    total = 0

    for i in range(len(isbn)):
        iterator = i + 1
        if not isbn[i].isdigit() and isbn[i] != 'X': 
            return False
        if isbn[i] == 'X':
            if iterator == len(isbn):
                total += (10 * iterator)
            else: return False
        else: 
            total += (int(isbn[i]) * iterator)

    if total % 11 == 0: return True
    return False

print(valid_ISBN10("1112223339")) # True
print(valid_ISBN10("111222333")) # False
print(valid_ISBN10("1112223339X")) # False
print(valid_ISBN10("1234554321")) # True
print(valid_ISBN10("1234512345")) # False
print(valid_ISBN10("048665088X")) # True
print(valid_ISBN10("X123456788")) # False
print(valid_ISBN10("ABCDEFGHIJ")) # False