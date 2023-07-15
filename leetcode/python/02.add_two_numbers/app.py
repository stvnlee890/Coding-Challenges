'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

EXAMPLE 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

EXAMPLE 2:
Input: l1 = [0], l2 = [0]
Output: [0]

EXAMPLE 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''
'''
TIME COMPLEXITY O(N)
- Traverses both l1 and l2 list inside a single while loop. 
- It's O(N) n being the longer list

SPACE COMPLEXITY O(N)
- Space required to store new linked list is proportional to the number of nodes in the longer list
'''

class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode()
        newNode = dummy_head
        carry_over = 0

        while l1 is not None or l2 is not None or carry_over > 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            sum = val1 + val2 + carry_over
            if sum > 9:
                sum = sum % 10
                carry_over = 1
            else: carry_over = 0
            newNode.next = ListNode(sum)
            newNode = newNode.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return dummy_head.next
            