class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return
            
            if remaining < 0:
                return 

            for i in range(start, len(nums)):
                path.append(nums[i])

                needed = remaining - nums[i]

                backtrack(i, needed, path)

                path.pop()
            
        
        backtrack(0, target, [])
        return result