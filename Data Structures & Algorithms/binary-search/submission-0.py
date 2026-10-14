class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums)-1

        while(s<=e):
            m = s + (e-s)//2

            if target == nums[m]:
                return m
            elif target > nums[m]:
                s = m+1
            else:
                e = m-1
        return -1
        