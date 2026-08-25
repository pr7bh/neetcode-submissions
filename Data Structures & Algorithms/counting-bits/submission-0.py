class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        def hammingWeight(n):
            count = 0
            while n!=0:
                if n&1 == 1:
                    count +=1
                n//=2
            return count

        for i in range(n+1):
            res.append(hammingWeight(i))
        return res
    