
"""
LeetCode Problem: 713. Subarray Product Less Than K
LeetCode Link: https://leetcode.com/problems/subarray-product-less-than-k/submissions/

Problem Description:
[Provide a brief description of the problem]

Solution:
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <=1:
            return 0
        product = 1
        count = 0
        left = 0
        for right in range(len(nums)):
            product *= nums[right] #update product

            #if product is >=k , move left +=1
            while product >=k:
                product /= nums[left]
                left +=1 

            count += (right - left +1)

        return count
"""

# Test cases
# Add test cases to validate your solution
