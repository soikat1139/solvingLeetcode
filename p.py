class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)

        i,j=0,1

        for k in nums:
            if k>0 :
                res[i]=k
                i+=2
            else:
                res[j]=k
                j+=2
        return res
