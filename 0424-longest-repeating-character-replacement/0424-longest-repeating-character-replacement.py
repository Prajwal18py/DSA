class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def find_max(freq):
            max_count = -1
            for i in range(256):
                max_count = max(max_count,freq[i])
            return max_count
        
        n = len(s)
        freq = [0] * 256
        high,low = 0,0
        res = float("-inf")

        for high in range(n):
            freq[ord(s[high])] +=1

            max_count = find_max(freq)
            length = high-low+1
            diff = length - max_count

            while diff > k:
                freq[ord(s[low])] -=1
                low+=1

                max_count = find_max(freq)
                length = high-low+1
                diff = length - max_count

            res = max(res,high-low+1)
        return res