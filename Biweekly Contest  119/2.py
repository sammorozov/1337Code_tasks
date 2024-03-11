class Solution:
    def removeAlmostEqualCharacters(self, word:str)->int:

        c,i=0,0

        while i<len(word)-1:
            
            if word[i]==word[i+1]:
                c+=1
                word=word[:i+1]+' '+word[i+2:]
                i+=1

            elif abs(ord(word[i])-ord(word[i+1]))==1:
                c+=1
                word=word[:i+1]+' '+word[i+2:]
                i+=1
                
            i+=1
        return c




print(Solution().removeAlmostEqualCharacters(word = "zyxyxyz"))