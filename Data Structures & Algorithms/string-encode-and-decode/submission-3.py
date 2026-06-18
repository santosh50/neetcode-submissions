class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for w in strs:
            res += str(len(w)) + '#' + w
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != '#':
                j += 1
            size = int(s[i:j])
            res.append(s[j + 1 : j + size + 1])
            i = j + size + 1
        return res

        
