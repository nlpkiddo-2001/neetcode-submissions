class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # creating graph and indegree
        graph = {}
        indegree = {}

        for word in words:
            for ch in word:
                graph[ch] = set()
                indegree[ch] = 0
        
        # building graph
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            
            length = min(len(word1), len(word2))

            for j in range(length):
                if word1[j] != word2[j]:
                    parent = word1[j]
                    child = word2[j]

                    if child not in graph[parent]:
                        graph[parent].add(child)
                        indegree[child] += 1
                    
                    break
        queue = deque()
        
        for ch in indegree:
            if indegree[ch] == 0:
                queue.append(ch)
        
        answer = []
        while queue:
            node = queue.popleft()
            answer.append(node)

            for neighbor in graph[node]:

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(answer) != len(graph):
            return ""
        return "".join(answer)

