class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sSet = {}
        tSet = {}
        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]
            if sChar in sSet:
                sSet[sChar] += 1
            else:
                sSet[sChar] = 0
            if tChar in tSet:
                tSet[tChar] += 1
            else:
                tSet[tChar] = 0
        
        return sSet == tSet
        
        