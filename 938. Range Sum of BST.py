# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        

        tot_summ = 0

        def dfs(node, tot_summ):
            if node:
                if low <= node.val <= high:
                    tot_summ += node.val 

                if node.left:
                    tot_summ += dfs(node.left, tot_summ)

                if node.righr:
                    tot_summ += dfs(node.right, tot_summ)


            return tot_summ
            
        return dfs(root, tot_summ)
        

        
        