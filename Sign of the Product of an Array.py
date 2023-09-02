class Solution:
    def arraySign(self, nums: List[int]) -> int:

        neg=0
        
        for i in nums:
            if i==0:
                return 0
            if i<0:
                neg+=1
        
        return 1 if neg%2==0 else -1

                
