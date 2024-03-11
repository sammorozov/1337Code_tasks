from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
это очень смешно


последний раз я менял этот файл 2 месяца назад и пытался решить через подсчет
количества всех элементов, что в целом алгоритмически даже лучше чем наивный подхолд
однако я понятия даже не имел как это можно сделать


это отчетливо видно в строчке for i in root

это пиздец кринж лол

'''
import math
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        summ = 0
        for i in root:
            if i is not None:
                summ += 1
        
        return int(math.log2(summ)) + 1
        
