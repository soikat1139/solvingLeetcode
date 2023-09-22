class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        sLen=len(s)
        tLen=len(t)
        

        def reccursive(sIndex,tIndex):

            if sIndex==sLen:
                return  True
            if tIndex==tLen:
                return False
            

            if s[sIndex]==t[tIndex]:
                sIndex+=1
                
            tIndex+=1
            return reccursive(sIndex,tIndex)

        return reccursive(0,0)
