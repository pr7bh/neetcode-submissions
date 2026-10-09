class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        bucket = [[] for _ in range(len(nums)+1)]
        hm = defaultdict(int)
        for num in nums:
            hm[num]+=1


        for key, value in hm.items():
            bucket[value].append(key)

        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                if(k != 0):
                    res.append(num)
                    k-=1

        return res