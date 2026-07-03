class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_inner(arr):

            prev2 = 0
            prev1 = 0

            for money in arr:
                current = max(prev1, money+prev2)
                prev2 = prev1
                prev1 = current
            
            return prev1
            
        return max(
            rob_inner(nums[1:]),
            rob_inner(nums[:-1])
        )