class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res=max(nums)

        currMax=1
        currMin=1

        for n in nums:

            if n==0:
                currMax=1
                currMin=1
                continue
            temp=n*currMax
            currMax=max(n,temp,n*currMin)
            currMin=min(n,temp,n*currMin)
            res=max(currMax,res)
        return res
