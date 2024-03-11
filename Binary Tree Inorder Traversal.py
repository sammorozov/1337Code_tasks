from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []

        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)

        inorder(root)
        return result


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)


node1.right = node2
node2.left = node3

solution = Solution()

res = solution.inorderTraversal(node1)

print(res)
