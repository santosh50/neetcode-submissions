class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        freqT = {}
        for c in t:
            freqT[c] = 1 + freqT.get(c, 0)
        
        window = {}
        l = 0
        res = ""
        resLen = float('inf')
        have = 0
        need = len(freqT)
        for r in range(len(s)):
            c = s[r]
            if c in freqT:
                window[c] = 1 + window.get(c, 0)
                if window[c] == freqT[c]:
                    have += 1
                
                while have == need:
                    windowLen = r - l + 1
                    if windowLen < resLen:
                        resLen = windowLen
                        res = s[l:r+1]
                    if s[l] in window:
                        window[s[l]] -= 1
                        if window[s[l]] < freqT[s[l]]:
                            have -= 1
                    l += 1
        return res


            




                        

            






        
        