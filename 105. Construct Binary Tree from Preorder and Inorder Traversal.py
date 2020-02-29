# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Medium
# Timedout first try using x for x in list if x in y. 
# Second try was faster by using slices. Had to look up solution. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        inorder_pivot = inorder.index(root_val)
        inorder_left = inorder[:inorder_pivot]
        inorder_right = inorder[inorder_pivot + 1:]
        
        preorder_left = preorder[1 : inorder_pivot + 1]
        preorder_right = preorder[inorder_pivot + 1:]
        
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root