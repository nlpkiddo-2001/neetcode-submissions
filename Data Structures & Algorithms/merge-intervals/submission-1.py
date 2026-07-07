class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # need to sort it
        # need to iterate it and check with interval[0] with the result_list[-1][1]
        # if less modify the result else append the result 
        
        intervals.sort(key=lambda x:x[0])
        result_list = []

        for interval in intervals:
            if not result_list:
                result_list.append(interval)
                continue

            if interval[0] <= result_list[-1][1]:
                result_list[-1][1] = max(interval[1], result_list[-1][1])
            else:
                result_list.append(interval)

        return result_list
            