'''
Given an array of integers nums and an integer target, return indices of the tow numbers such that they add up to the target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''

'''
Create a hash map
key: index
Create global variable that stores the result. 
Check the dictionary for that result variable, if != None then we know we've found the other pair.
'''

class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            result = target - nums[i]
            if map.get(result) != None:
                return [map.get(result), i]
            else:
                map[nums[i]] = i


solution = Solution()
print(solution.twoSum([2, 11, 15, 7], 9))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3, 3], 6))
