class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        nodelete = arr[0]
        onedelete = float("-inf")
        ans = arr[0]

        for i in range(1,len(arr)):
            prev_nodel = nodelete

            nodelete = max(arr[i],nodelete + arr[i])
            onedelete = max(onedelete + arr[i],prev_nodel)

            ans = max(ans,nodelete,onedelete)
        return ans