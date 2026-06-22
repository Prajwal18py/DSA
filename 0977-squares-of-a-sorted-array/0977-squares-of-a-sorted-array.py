from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos = []
        neg =[]
        res = []
        for i in range(0,len(nums)):
            if nums[i] >= 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])

        if len(pos) == 0:
            res = [x*x for x in neg]
            res.reverse()
            return res
        if len(neg) == 0:
            return [x*x for x in pos]

        pos= [x*x for x in pos]
        neg = [x*x for x in neg][::-1]

        n = len(neg)
        m = len(pos)

        i,j = 0,0
        while i < n and j < m:
            if neg[i] <= pos[j]:
                res.append(neg[i])
                i+=1
            else:
                res.append(pos[j])
                j+=1
        while i < n:
            res.append(neg[i])
            i+=1
        while j < m:
            res.append(pos[j])
            j+=1

        return res
        

        

        
        