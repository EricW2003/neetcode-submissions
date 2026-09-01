import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.nums = nums
        self.kth = None
        while len(self.nums)>= self.k:
            self.kth = heapq.heappop(self.nums)
    def add(self, val: int) -> int:
        if self.kth is None or val > self.kth:
            heapq.heappush(self.nums, val)
            self.kth = heapq.heappop(self.nums)
        return self.kth
