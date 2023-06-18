
"""
LeetCode Problem: Minimum Distance Between BST Nodes
LeetCode Link: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

Problem Description:
[Provide a brief description of the problem]

Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node, prev, mini):
            if node is None:
                return mini
            mini = inorder(node.left, prev, mini)

            if prev is not None:
                mini = min(mini, node.val - prev )
            prev = node.val

            mini = inorder(node.right,prev, mini)

            return mini
        
        return inorder(root,None, float('inf'))

"""

# Test cases
# Add test cases to validate your solution
