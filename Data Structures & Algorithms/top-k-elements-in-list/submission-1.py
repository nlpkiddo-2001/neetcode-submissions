class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_count = freq_map.get(num)
                freq_map[num] = freq_count + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq_map.items():
            buckets[count].append(num)
        
        results = []
        for count in range(len(nums), -1, -1):
            for num in buckets[count]:
                results.append(num)
                if len(results) == k:
                    return results
