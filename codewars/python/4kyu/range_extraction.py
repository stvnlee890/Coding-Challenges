# Range Extraction
#
# A format for expressing an ordered list of integers is to use a comma separated list of either:
# - individual integers
# - or a range of integers denoted by the starting integer separated from the end integer in the range
#   by a dash, "-". The range includes all integers in the interval inclluding both endpoints. It is not 
#   considered a range unless it spans at least 3 numbers. For exampe "12,13,15-17"
#
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted
# string int the range format.

def solution(args):
    start = 0
    scout = 0
    counter = 0
    extract = ''

    while (scout < len(args)):
        while (scout + 1 < len(args) and args[scout + 1] - args[scout] == 1):
            counter += 1
            scout += 1
        
        print(start, scout)
        if (counter >= 2):
            extract += f"{args[start]}-{args[scout]},"
            start = scout + 1
            scout = start
        elif (counter == 1):
            extract += f"{args[start]},{args[scout]},"
            start = scout + 1
            scout = start
        else:
            extract += f"{args[start]},"
            start = scout + 1
            scout = start

        counter = 0
    extract = extract[:-1]
    print(extract)
    return extract




solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 20,])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
