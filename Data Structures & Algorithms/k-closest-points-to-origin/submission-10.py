import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for val in points:
            x = val[0]
            y = val[1]
            print(val)
            heapq.heappush(heap,(-(x**2+y**2),x,y))
            if len(heap)>k:
                heapq.heappop(heap)

        ans = []

        while heap:
            _, x,y = heapq.heappop(heap)
            ans.append([x,y])
            
        return ans