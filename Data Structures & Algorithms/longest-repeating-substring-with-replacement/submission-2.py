class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        freq = {}
        maxf = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxf = max(freq[s[r]], maxf)
            while (r - l + 1) - maxf > k:
                freq[s[l]] -= 1
                l += 1
            longest = max(r - l + 1, longest)
        return longest


        