
"""
LeetCode Problem: 658. Find K Closest Elements
LeetCode Link: https://leetcode.com/problems/find-k-closest-elements/submissions/

Problem Description:
[Provide a brief description of the problem]

Solution:
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0 , len(arr) - k
        while left < right:
            mid = left + (right - left) // 2
            # Check if the left element is closer to x than the right element
            if x - arr[mid] > arr[mid+k] - x:
                left = mid +1 
            else:
                right = mid 

        return arr[left:left + k]

"""

# Test cases
# Add test cases to validate your solution
