import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        k = 0
        ans = 0

        task_list = [0]*26
        for task in tasks:
            task_list[ord(task)-ord("A")]+=1

        heap = []
        heapq.heapify(heap)

        for letter, freq in enumerate(task_list):
            if freq!=0:
                heapq.heappush(heap,(-freq,letter))

        waiting_list = deque([])

        while k<len(tasks):
            if waiting_list and waiting_list[0][2]==ans:
                freq, letter,_ = waiting_list.popleft()
                heapq.heappush(heap,(freq,letter))
            if heap:
                freq, letter = heapq.heappop(heap)
                if freq<-1:
                    waiting_list.append((freq+1,letter,ans+n+1))
                k+=1
            ans+=1
        return ans

