class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        max_diff = float("inf")

        for i in range(0,n-2):
            left = i+1
            right = n-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                diff = abs(target - total)

                if diff < max_diff:
                    max_diff = diff
                    result = total
                
                if total == target:
                    return result
                
                if total < target:
                    left+=1
                else:
                    right-=1
        return result