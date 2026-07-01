import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        if self.right and (-self.left[0] > self.right[0]):
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        
        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        elif len(self.right) > len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)
    


    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return float(-self.left[0])
        else:
            return (-self.left[0] + self.right[0]) / 2.0
        