class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        def helper(big_list):
            big_list.sort(key=lambda x : x[0])
            result_list = []

            for interval in big_list:
                if not result_list:
                    result_list.append(interval)
                    continue
                
                if interval[0] <= result_list[-1][1]:
                    result_list[-1][1] = max(interval[1], result_list[-1][1])
                else:
                    result_list.append(interval)
            
            return result_list

        intervals.append(newInterval)
        return helper(intervals)

        