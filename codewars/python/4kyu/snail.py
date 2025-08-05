# Snail sort
#
# Given a nxn array, return the array elements from outermost elements
# to middle element, traveling clockwise. 
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
#
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
#
# array = [[1,2,3],
#         [8,9,4],
#         [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
#
# array = [[1,  2,  3,  4],
#          [5,  6,  7,  8],
#          [9,  10, 11, 12],
#          [13, 14, 15, 16]]
#
# array = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
#
# snail(array) #=> [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
#
# array = [[1,  2,  3,  4, x],
#          [5,  6,  7,  8, x],
#          [9,  10, 11, 12, x],
#          [13, 14, 15, 16, x],
#          [x,  x,  x,  x,  x]],
#
# array = [[1,  2,  3,  4, x, x],
#          [5,  6,  7,  8, x, x],
#          [9,  10, 11, 12, x, x],
#          [13, 14, 15, 16, x, x],
#          [x,  x,  x,  x,  x, x]
#          [x,  x,  x,  x,  x, x],

#
# # 3x3 array
#
# Add j
# i=0 j=0
# i=0 j=1
# i=0 j=2
#
# Add i
# i=1 j=2
# i=2 j=2
#
# Subtract j
# i=2 j=1
# i=2 j=0
#
# Add j
# i=1 j=0
# i=1 j=1


# 4x4 array
# i=0 j=0
# i=0 j=1
# i=0 j=2
# i=0 j=3
#
# i=1 j=3
# i=2 j=3
# i=3 j=3
#
# i=3 j=2
# i=3 j=1
# i=3 j=0
# 
# i=2 j=0
# i=1 j=0
#
# i=1 j=1
# i=1 j=2
#
# i=2 j=2
# i=2 j=1
#

# When adding, we add up to the "end" of the array.  When subtracting, we subtract up to the "beggining"
# Need to find a way to keep track of new beginnings and new ends
#
def snail(snail_map):
    map_length = len(snail_map)
    sorted_arr = []
    j = 0
    i = 0

    x = 0
    y = map_length - 1

    if len(snail_map[i]) == 0:
        return sorted_arr
    
    while(len(sorted_arr) < map_length**2):
        if (y != map_length -1 and len(sorted_arr) != map_length - 1):
            sorted_arr.pop()
        while (j < y):
            sorted_arr.append(snail_map[i][j])
            j+= 1
        while (i < y):
            sorted_arr.append(snail_map[i][j])
            i+= 1
        while (j > x):
            sorted_arr.append(snail_map[i][j])
            j-= 1
            if (j == x):
                x+= 1
        while (i > x):
            sorted_arr.append(snail_map[i][j])
            i-= 1
            if (i == x):
                y-= 1
        sorted_arr.append(snail_map[i][j])
    return sorted_arr

print(snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(snail([[1, 2, 3], [8, 9, 4], [7, 6, 5]]))
print(snail([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
print(snail([[]]))
