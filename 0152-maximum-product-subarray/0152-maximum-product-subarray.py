class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_ending,max_ending  = nums[0],nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            prev_min = min_ending
            prev_max = max_ending

            v1 = nums[i]
            v2 = prev_min * nums[i]
            v3 = prev_max * nums[i]

            max_ending = max(v1,v2,v3)
            min_ending = min(v1,v2,v3)

            ans = max(ans,max(max_ending,min_ending))
        
        return ans