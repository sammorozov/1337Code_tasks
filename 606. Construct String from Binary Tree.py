from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        def preorder(node):
            if not node:
                return ""

            result = str(node.val)

            if node.left or node.right:
                result += "(" + preorder(node.left) + ")"

            if node.right:
                result += "(" + preorder(node.right) + ")"

            return result

        return preorder(root)
    

# Создание узлов
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

# Установка связей между узлами
node1.left = node2
node1.right = node3
node2.left = node4

# Создание экземпляра класса Solution
solution = Solution()

# Получение строки из дерева
result = solution.tree2str(node1)
print(result)  # Результат: "1(2(4))(3)"
