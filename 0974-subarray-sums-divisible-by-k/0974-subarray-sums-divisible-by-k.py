class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total,res = 0,0
        freq = {}
        freq[0] = 1

        for i in range(len(nums)):
            total += nums[i]
            rem = total % k

            if rem < 0:
                rem = rem + k
            
            res += freq.get(rem,0)
            freq[rem] = freq.get(rem,0) + 1
        
        return res