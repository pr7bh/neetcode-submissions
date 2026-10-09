class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr = 0
        hm= defaultdict(int)
        hm[0] = 1

        for i in nums:
            curr+=i
            res += hm[curr-k]
            hm[curr] += 1

        return res

