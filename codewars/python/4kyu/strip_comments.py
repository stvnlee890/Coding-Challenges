'''
4kyu Strip Comments

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 
any whitespace at the end of the line should also be stripped out.

Example: 

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples

The output expected would be:
apples, pears
grapes
bananas
'''

def strip_comments(strng, markers):
    new_line = '\n'
    start = 0
    scout = 0

    stripped = ""

    while(scout < len(strng)):
        if strng[scout] in markers:
            # check remove whitespace in stripped
            print(start, strng[scout])
            while(strng[scout] is not new_line and scout < len(strng) - 1):
                scout += 1

        if not scout - start == 1:
            start = scout
        else:
            stripped += strng[start]
            
        if scout == len(strng) - 1 and scout - start == 1:
            start = scout
            stripped += strng[start]

        start = scout
        scout += 1

    print(stripped)
    pass

# # 'apples, pears\ngrapes\nbananas'
# strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])
# #  'a\nc\nd'
# strip_comments('a #b\nc\nd $e f g', ['#', '$'])
# # ' a\nc\nd'
# strip_comments(' a #b\nc\nd $e f g', ['#', '$'])

# strip_comments("  pears ' @ , watermelons oranges\n# # oranges oranges oranges @\npears ? watermelons apples @\npears pears oranges pears", [])

# strip_comments("- ,\npears\n' oranges - apples avocados\n-", ['=', "'", '!', '^', '?', '@'])

# strip_comments(", bananas strawberries cherries\navocados strawberries ? strawberries watermelons oranges\n' # ' cherries strawberries avocados\n, @ watermelons ,", ['=', '.', ',', '-', '@', '?'])

strip_comments("  # -\nwatermelons ? cherries\n^ lemons .\n.\n, ' strawberries # apples pears", [',', '!', '?', "'"])