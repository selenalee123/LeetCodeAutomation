
"""
LeetCode Problem: 104. Maximum Depth of Binary Tree
LeetCode Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursively
        # if root is None:
        #     return 0
        # return 1 + max(self.maxDepth(root.right) , self.maxDepth(root.left))

        # iteration 
        stack = []
        if root is not None: 
            stack.append((1,root))
        depth = 0
        while stack:
            # keep track current depth level 
            cur_depth, node = stack.pop()
            if node is not None:
                # maximum depth vs cur depth
                depth = max(cur_depth,depth)
                #increment current depth for left and right node
                if node.left:
                    stack.append((cur_depth +1 ,node.left))
                if node.right:
                    stack.append((cur_depth +1 ,node.right))
        return depth












         # stack = []
        # if root is not None:
        #     stack.append((1,root))
        # depth = 0
        # while stack != []:
        #     cur_dep , root = stack.pop()
        #     if root is not None:
        #         depth = max(depth, cur_dep)
        #         stack.append((cur_dep + 1 , root.left))
        #         stack.append((cur_dep +1 , root.right))
        # return depth 
"""

# Test cases
# Add test cases to validate your solution
