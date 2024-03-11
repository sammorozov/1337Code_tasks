from typing import *
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        cnt = 0
        
        for pair in paths:

            second_sity = pair[1]

            for pair_2 in paths:
                if pair_2[0] == second_sity:
                    break

                else:
                    cnt +=1

            
            if cnt == len(paths):
                return second_sity
            else:
                cnt = 0

print(Solution().destCity(paths = [["B","C"],["D","B"],["C","A"]]))



'''

there is some code for show how set works and how zip works


'''
print('^the answer^_______________________')


a = {2, 3, 4}

b = {1, 2, 3, 4}

c = {1, 2, 3, 4}

d = {2, 3, 4}


print(a - b)

print(c - d)

print('_______________')

paths = [["B","C"],["D","B"],["C","A"]] 
frm = zip(*paths)
print(list(frm))

print(*paths)
# print(to)


frm, where = zip(*paths)
print('________________')
print(frm)
print(where)