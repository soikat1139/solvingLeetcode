class Solution:
    def isValid(self, s: str) -> bool:
        hashMap={
            "(":")",
            "[":"]",
            "{":"}"
        }
        stack=[]

        for c in s:

            if c in hashMap:
                stack.append(hashMap[c])
            else:
                if stack and stack[-1]==c:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
