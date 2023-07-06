class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        aPointer=0

        for i in range(len(t)):
            if t[i]==s[aPointer]:
                aPointer+=1
            if aPointer==len(s):
                return True
        return False
