class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(0,n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            left = i+1
            right = n-1
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                        
                    while left < n and nums[left] == nums[left-1]:
                        left+=1
                    while right >= 0 and nums[right] == nums[right+1]:
                        right-=1
                elif nums[left] + nums[right] > target:
                    right-=1
                else:
                    left+=1
        return result

        