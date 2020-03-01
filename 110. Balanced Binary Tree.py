# https://leetcode.com/problems/balanced-binary-tree/
# Easy
# Slow but good memory usage
# 1st time, I didn't check for []
# 2nd time, I knew would fail but tried it anyways. I didn't check the subtrees for imbalance


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        def treeHeight(root):
            if not root:
                return 0
            return 1 + max(treeHeight(root.left), treeHeight(root.right))
        
        if abs(treeHeight(root.left) - treeHeight(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)