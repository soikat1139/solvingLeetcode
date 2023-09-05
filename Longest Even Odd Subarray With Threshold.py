class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        prev_even=False

        res,count=0,0

        for num in nums:
            even=(num%2)==0

            if num>threshold or even==prev_even:
                res=max(res,count)
                count=0
               
            
            count+=(num<=threshold) and (even or count>0)
            prev_even=even

        return max(res,count)
