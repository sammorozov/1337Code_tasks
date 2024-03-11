# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
        
#         n = 0
#         node = root
#         number = 0
#         depths = []
#         def bst(node, number, depths):
#             if node.left:
#                 node = node.left
#                 number += 1
            

#             elif node.right:
#                 node = node.right
#                 number += 1

#             else:
#                 depths.append(number)
                
#             return bst(node, number, depths)
        
#         bst(root, 0, depths)
#         return max(depths)
from typing import *

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bst(node, depth):
            if not node:
                return depth
            left_depth = bst(node.left, depth + 1)
            right_depth = bst(node.right, depth + 1)
            return max(left_depth, right_depth)

        return bst(root, 0)