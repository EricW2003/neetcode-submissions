class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x :x[0])
        start , end = intervals[0][0], intervals[0][1]
        ans = 0
        print(intervals)
        for i in range(1,len(intervals)):
            start_i, end_i = intervals[i]

            if end>start_i:
                ans+=1
                end = min(end,end_i)
            else:
                start, end = start_i, end_i
        return ans