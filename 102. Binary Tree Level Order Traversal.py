# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Medium
# Notes: uses multiple lists and did it using iterative methods.
# Notes: 1 list to carry nodes and another to hold children. Must empty lists each iteration
# Notes: Good time and space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        answer = []
        
        queue = []
        queue.append(root)
        children = []
        
        while queue:
            level_nodes = []
            for node in queue:
                level_nodes.append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            if level_nodes:
                answer.append(level_nodes)
            
            queue = children
            children = []
            
        return answer