class Solution:
    def partitionString(self, s: str) -> int:
        visitSet=set()

        res=1

        for c in s:
            if c in visitSet:
                res+=1
                visitSet=set()
            visitSet.add(c)
        
        return res
        
