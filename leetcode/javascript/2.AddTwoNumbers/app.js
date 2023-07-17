/*
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
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/*
TIME COMPLEXITY: O(N)
    - Traverses the longer list in a single loop
SPACE COMPLEXITY: O(N)
    - Creates a new list based on N lenght
*/

var addTwoNumbers = function(l1, l2) {
    // Create a placeholder node
    let dummyHead = new ListNode()
    // Create actual node that references placeholder node so that we don't lose reference to the first node. 
    // If we initialize node = new ListNode(), the new node we create in the while loop will break the reference to first node
    let node = dummyHead
    let carryOver = 0

    while(l1 || l2 || carryOver > 0) {
        let val1 = l1 ? l1.val : 0
        let val2 = l2 ? l2.val : 0
        let sum = val1 + val2 + carryOver

        if(sum > 9) {
            sum = sum % 10
            carryOver = 1
        } else {
            carryOver = 0
        }

        node.next = new ListNode()
        node = node.next
        
        if(l1) l1 = l1.next
        if(l2) l2 = l2.next
    }
    return dummyHead.next
}