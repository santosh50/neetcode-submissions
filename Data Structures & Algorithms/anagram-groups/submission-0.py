class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for w in strs:
            s = ''.join(sorted(w))
            if s in seen:
                seen[s].append(w)
            else:
                seen[s] = [w]
        return list(seen.values())
        