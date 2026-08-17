class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        zero,one = 0,0
        res = 0
        freq = {}

        for i in range(n):
            if nums[i] == 0:
                zero += 1
            else:
                one += 1
            
            diff = zero - one

            if diff == 0:
                res = max(res, i+1)
                continue
            
            if diff in freq:
                res = max(res , i - freq[diff])
            else:
                freq[diff] = i
        
        return res
        