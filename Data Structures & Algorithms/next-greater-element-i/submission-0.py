class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = {}
        stack = []

        for x in nums2:
            while stack and stack[-1]<x:
                nge[stack.pop()] = x
            stack.append(x)

        return [nge.get(x,-1) for x in nums1]