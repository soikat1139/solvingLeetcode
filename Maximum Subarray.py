class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub=nums[0]

        currSum=0

        for i in nums:
            if currSum<0:
                currSum=0
            currSum=currSum+i
            maxSub=max(currSum,maxSub)
        return maxSub
