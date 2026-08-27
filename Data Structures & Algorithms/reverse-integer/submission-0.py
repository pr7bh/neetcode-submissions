class Solution:
    def reverse(self, n: int) -> int:
        isNegative = 0
        if n < 0:
            isNegative = 1
        n = abs(n)
        m = 0
        while n != 0:
            r = n%10
            m = m*10+r
            n//=10
        if isNegative:
            m = -m
        if m > 2**31 or m < -2**31:
            return 0
        return m

