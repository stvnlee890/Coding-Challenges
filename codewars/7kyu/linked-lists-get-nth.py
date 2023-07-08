'''
Linked Lists - Get Nth
Implement a GetNth() function that takes a linked list and an integer index
and returns the node stored at the Nth index position. GetNth() uses the C numbering
convenetion that the first node is index 0, the second is index 1, ... and so on.

So for the list 42 -> 13 -> 666, GetNth(1) should return Node(13)

getNth(1 -> 2 -> 3 -> null, 0).data === 1
getNth(1 -> 2 -> 3 -> null, 1).data === 2

The index should be in the range [0...length-1]. If it is not, or if the list 
is empty, GetNth() should throw/raise an exception (ArgumentException) in
c#, InvalidArgumentException in PHP, Exception in Java).
'''

def get_nth(node, index):
    if index < 0:
        raise Exception("Invalid index")
    if index == 0 and not node:
        raise Exception("Node is None")
    if index == 0:
        return node
    if index == 1:
        return node.next
    else:
        for i in range(index):
            node = node.next
            if (index - 1) - 1 == 1 and not node.next:
                raise Exception("Invalid index value")
            if i == index - 1:
                return node

# Clever answers by other user using recursion
def get_nth(node, index):
    if node and index >= 0: 
        return node if index < 1 else get_nth(node.next, index - 1)