class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left=0
        right=0
        best = 0

        for ch in s:
            if ch in last and last[ch]>=left:
                left = last[ch]+1
            last[ch] = right

            window = right - left + 1
            if window > best:
                best = window
            right+=1

        return best