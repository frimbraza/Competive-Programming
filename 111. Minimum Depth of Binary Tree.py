# Minimum Depth Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# 3 tries (1st: didn't understand q., 2nd: edge case)
# Kinda slow and not good memory usage(recursive)
# Need to do iterative for better result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        if not left and not right:
            return 1
        elif left and right:
            return 1 + min(left, right)
        elif left:
            return 1 + left
        else:
            return 1 + right