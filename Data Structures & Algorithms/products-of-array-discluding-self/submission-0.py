class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        out = [1] * n

        for i in range(n):
            for j in range(n):
                if i!=j:
                    out[i]*=nums[j]
        return out