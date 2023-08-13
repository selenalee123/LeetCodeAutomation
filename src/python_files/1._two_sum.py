
"""
LeetCode Problem: 1. Two Sum
LeetCode Link: https://leetcode.com/problems/two-sum/

Problem Description:
[Provide a brief description of the problem]

Solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[val] = i 

        return []
        
"""

# Test cases
# Add test cases to validate your solution
