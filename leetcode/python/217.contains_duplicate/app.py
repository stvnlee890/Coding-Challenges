'''
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

EXAMPLE 1:
Input: nums = [1,2,3,1]
Output: true

EXAMPLE 2:
Input: nums = [1,2,3,4]
Output: false

EXAMPLE 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

TIME COMPLEXITY: O(N)
 - Traverses list N times

SPACE COMPLEXITY: O(N)
- Worst case is all elements in nums list are stored in dictionary
'''

class Solution(object):
    def containsDuplicate(self, nums):
        obj = {}
        for i in nums:
            if i not in obj:
                obj[i] = 1
            else:
                return True

# OR another way is to create a set. 
class Solution(object):
    def containsDuplicate(self, nums):
        hset = set()
        for i in nums:
            if i not in hset:
                hset.add(i)
            else:
                return True