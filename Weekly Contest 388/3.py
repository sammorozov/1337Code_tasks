from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        def all_substrings(s):
            res = [
                s[i: j] for i in range(len(s))
                for j in range(i + 1, len(s) + 1)
            ]
            
            return res
        out = ['' for i in range(len(arr))]
        for i in range(len(arr)):
            all_vars = all_substrings(arr[i])
            for var in all_vars:
                for control in arr:
                    if control == arr[i]:
                        
                        continue
                    flag = True
                    if var in control:
                        flag = False
                        break
                    else:
                        continue
                if flag:
                    if out[i] == '':
                        out[i] = var
                    elif out[i] != '':
                        if len(out[i]) < len(var):
                            pass
                        elif len(out[i]) > len(var):
                            out[i] = var
                        elif len(out[i]) == len(var):
                            if out[i] < var:
                                pass
                            else:
                                out[i] = var



        return out


                        
                

                

print(Solution().shortestSubstrings(["fhi","ct","s","o","o"]))