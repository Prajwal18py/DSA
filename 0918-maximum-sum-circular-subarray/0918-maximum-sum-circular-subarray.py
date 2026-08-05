class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        current_max = best_max = nums[0]
        current_min = best_min = nums[0]
        total_sum = sum(nums)

        for i in range(1,len(nums)):
            current_max = max(nums[i],current_max + nums[i])
            best_max = max(best_max,current_max)

            current_min = min(nums[i],current_min + nums[i])
            best_min = min(best_min,current_min)
        
        circular = total_sum - best_min
        
        if best_max > 0:
            ans = max(best_max , circular)
        else:
            ans = best_max
        
        return ans

            

        