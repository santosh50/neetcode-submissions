class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for w in strs:
            count = [0] * 26
            for ch in w:
                count[ord(ch) - ord('a')] += 1
            tup = tuple(count)
            if tup in seen:
                seen[tup].append(w)
            else:
                seen[tup] = [w]
        return list(seen.values())
        