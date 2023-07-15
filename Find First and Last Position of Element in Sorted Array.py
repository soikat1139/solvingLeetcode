class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l=0
        r=len(nums)-1
        mid=0
        found=False

        while l<r:
            mid=(l+r)//2

            if nums[mid]>target:
                r=mid-1
            if nums[mid]<target:
                l=mid+1
            if nums[mid]==target:
                found=True
                break
        
        l=mid
        r=mid

        while l-1>=0:
            if nums[l-1]==target:
                l=l-1
            else:
                break
        while r+1<len(nums):
            if nums[r+1]==target:
                r=r+1
            else:
                break
        print(found)

  
        
        return [l,r] if found else [-1,-1]
        
