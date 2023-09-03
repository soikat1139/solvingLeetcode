class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        l=0
        r=len(nums)-1

        res=[]

        while l<=r:
            
            if nums[l]*nums[l] >nums[r]*nums[r]:
                res.append(nums[l]*nums[l])
                l+=1
            else:
                res.append(nums[r]*nums[r])
                r-=1

        
        return res[::-1]
        
