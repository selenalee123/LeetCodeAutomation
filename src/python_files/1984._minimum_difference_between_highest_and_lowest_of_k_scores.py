
"""
LeetCode Problem: 1984. Minimum Difference Between Highest and Lowest of K Scores
LeetCode Link: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/submissions/

Problem Description:
[Provide a brief description of the problem]

Solution:
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) <=1:
            return 0
        nums.sort()
        min_diff = float('inf')
        
        for i in range(len(nums)-k+1):
            diff = nums[i+k-1] - nums[i]
            min_diff = min(diff,min_diff )
        return min_diff

"""

# Test cases
# Add test cases to validate your solution
