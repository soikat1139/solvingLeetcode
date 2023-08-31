class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = 0

        res = []

        i = len(num)-1

        for n in range(max(len(num), len(str(k)))):

            digit1 = num[i] if i>= 0 else 0

            digit2 = k%10 if k else 0

            sum = digit1+digit2+carry

            carry = sum//10

            sum = sum%10 if sum>=10 else sum

            res.append(sum)

            i -= 1

            k = k//10 if k else 0



        if carry:

            res.append(carry)

        return res[::-1]
