class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        out = [1] * n

        prefix = 1
        for i in range(n):
            out[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for j in range(n-1, -1, -1):
            out[j] *= suffix
            suffix *= nums[j]

        return out