class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=[s for s in range(1,n+1)]
        res=[]

        def backTrack(start,comb):
            if len(comb)==k:
                res.append(comb.copy())
                return
            if start>=len(nums):
                return
            
            comb.append(nums[start])

            backTrack(start+1,comb)
            comb.pop()
            backTrack(start+1,comb)
            
        backTrack(0,[])
        return res
