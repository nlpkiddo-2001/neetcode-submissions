class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, num in enumerate(nums):
            curr = target - num
            if curr in hash_map:
                return [hash_map.get(curr), index]
            hash_map[num] = index
        return [-1, -1]