class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
        # res = 0
        # left, right = 0, len(heights) - 1

        # while left < right:
        #     area = min(heights[left], heights[right]) * (right - left)
        #     res = max(res, area)
        #     if heights[left] <= heights[left]:
        #         left += 1
        #     else:
        #         right -= 1

        # return res