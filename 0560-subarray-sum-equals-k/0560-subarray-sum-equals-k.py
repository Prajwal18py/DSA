class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum ,result = 0,0
        
        freq = {}
        freq[0] = 1


        for num in nums:
            prefix_sum += num
            ques = prefix_sum - k

            result += freq.get(ques,0)
            
            freq[prefix_sum] = freq.get(prefix_sum,0) + 1
        
        return result
        