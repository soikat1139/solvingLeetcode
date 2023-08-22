class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()

        res=[]

        for s in spells:
            idx=len(potions)

            l,r=0,len(potions)-1

            while l<=r:
                m=(l+r)//2

                if s*potions[m]>=success:
                    idx=m
                    r=m-1
                else:
                    l=l+1
            res.append(len(potions)-idx)
        
        return res
