
"""
LeetCode Problem: 2269. Find the K-Beauty of a Number
LeetCode Link: https://leetcode.com/problems/find-the-k-beauty-of-a-number/description/

Problem Description:
[Provide a brief description of the problem]

Solution:
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        for i in range(len(num)-k+1):
            substring = num[i:i+k]

            sub_num = int(substring)
            if if sub_num != 0 and num % sub_num == 0:
                count +=1

        return count

            
"""

# Test cases
# Add test cases to validate your solution
