class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        heap = []
        ans = []

        start, end = float("-inf"), float("inf")

        for interval in intervals:
            start_i, end_i = interval[0], interval[1]
            if end>= start_i:
                if start == float("-inf"):
                    start = start_i
                    end = end_i
                else:
                    start = min(start,start_i)
                    end = max(end,end_i)
            else:
                ans.append([start,end])
                start, end = start_i, end_i
        ans.append([start,end])
        start, end = float("-inf"), float("inf")
        return ans