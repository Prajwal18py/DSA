class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low,high = 0,0
        result = float("inf")
        total = 0
        n = len(nums)

        while high < n:
            total += nums[high]
            
            while total >= target:
                length = high-low+1
                result = min(result,length)

                total-= nums[low]
                low+=1
            high+=1
        
        return 0 if result == float("inf") else result

        