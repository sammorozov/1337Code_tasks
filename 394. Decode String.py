class Solution:
    def decodeString(self, s: str) -> str:
        
        s = s.replace('[', '*("').replace(']', '")+')

        if s[-1] == '+':
            s = s[:-1]
        decoded = eval(s) # эта хуйня умеет исполнять python код внутри python кода я в ахуе
        return decoded
    
print(Solution().decodeString(s = "3[a2[c]]"))
