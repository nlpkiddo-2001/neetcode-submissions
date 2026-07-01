class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}
        for course, prequi in prerequisites:
            graph[course].append(prequi)
        
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False
            elif state[course] == 2:
                return True
            
            state[course] = 1

            for nei in graph[course]:
                if not dfs(nei):
                    return False
            
            state[course] = 2

            return True
        
        for c in range(numCourses):
            if state[c] == 0:
                if not dfs(c):
                    return False

        return True
            
