 class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap={}
        

        for i,v in enumerate(nums):
            
            desired=target-v
            if desired in hashMap:
                return [i,hashMap[desired]]
            hashMap[v]=i
            
