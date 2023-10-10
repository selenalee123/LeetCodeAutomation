
"""
LeetCode Problem: 647. Palindromic Substrings
LeetCode Link: https://leetcode.com/problems/palindromic-substrings/description/

Problem Description:
[Provide a brief description of the problem]

Solution:
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            # odd len of string 
            l , r = i , i

            while l >= 0 and r <len(s) and s[l] == s[r]:
                l -=1
                r +=1
                result +=1   
            # // even len of string
            l , r = i , i +1 

            while l >= 0 and r <len(s) and s[l] == s[r]:
                l -=1
                r +=1
                result +=1
        return result
        
"""

# Test cases
# Add test cases to validate your solution
