class Solution:
    def countSubstrings(self, s: str) -> int:
        

        def manacher_odd(s):
            s = '$' + s + '^'
            n = len(s)
            res = [0] * n
            l = 0
            r = 0
            for i in range(1, n - 1):
                res[i] = max(0, min(r - i, res[l + (r - i)]))
                while s[i - res[i]] == s[i + res[i]]:
                    res[i] += 1
                if i + res[i] > r:
                    l = i - res[i]
                    r = i + res[i]
            return res[1:-1]

        def manacher(s):
            res = manacher_odd('#' + '#'.join(s) + '#')[1:-1]
            return ([x // 2 for x in res[::2]], [x // 2 for x in res[1::2]])
        sm = 0
        for lst in manacher(s):
            sm += sum(lst)

        return sm
    
print(Solution().countSubstrings('aaa'))