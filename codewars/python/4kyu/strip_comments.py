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

# essentially remove everything after comment marker up to new_line
def strip_comments(strng, markers):
    new_line = '\n'
    
    # two pointer method
    # scout pointer scouts for markers.
    # place start pointer to scout
    #   scout iterates until new_line expected
    #   scout always checks for end of string
    
    start = 0
    scout = 0
    
    stripped = ""

    while(scout < len(strng)):
        if strng[scout] in markers:
            while(start < scout):
                stripped += strng[start]
                start += 1

            
        scout += 1

    print(stripped)
    pass

# 'apples, pears\ngrapes\nbananas'
strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])
#  'a\nc\nd'
strip_comments('a #b\nc\nd $e f g', ['#', '$'])
# ' a\nc\nd'
strip_comments(' a #b\nc\nd $e f g', ['#', '$'])
