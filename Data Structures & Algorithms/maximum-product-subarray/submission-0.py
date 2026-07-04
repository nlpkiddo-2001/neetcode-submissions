class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        answer = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(num, num*max_product)
            min_product = min(num, num*min_product)

            answer = max(answer, max_product)
        return answer