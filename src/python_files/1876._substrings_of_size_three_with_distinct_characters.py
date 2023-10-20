
"""
LeetCode Problem: 1876. Substrings of Size Three with Distinct Characters
LeetCode Link: https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/

Problem Description:
[Provide a brief description of the problem]

Solution:
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(2,len(s)):
            if s[i] != s[i-1] and s[i] != s[i-2] and s[i-1] != s[i-2]:
                count +=1
        return count
        
"""

# Test cases
# Add test cases to validate your solution
