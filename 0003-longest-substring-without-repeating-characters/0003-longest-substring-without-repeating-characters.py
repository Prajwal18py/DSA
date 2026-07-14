class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low,high = 0,0
        res = 0
        freq = {}

        for high in range(len(s)):
            freq[s[high]] = freq.get(s[high],0)+1
            k = high-low+1
            while len(freq) < k:
                freq[s[low]] -=1
                if freq[s[low]] == 0:
                    del freq[s[low]]
                low+=1
                k = high-low+1
            res = max(res,high-low+1)
        return res