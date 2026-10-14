class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(first):
            s = 0
            e = len(nums) - 1
            ans = -1
            while s<=e:
                m = (s+e)//2
                if target == nums[m]:
                    ans = m
                    if first:
                        e = m-1
                    else:
                        s = m+1
                elif target>nums[m]:
                    s = m+1
                else:
                    e = m-1
            return ans
        return [first(True),first(False)]

        