class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x :x[0])
        end = intervals[0][1]
        ans = 0
        for i in range(1,len(intervals)):
            start_i, end_i = intervals[i]

            if end>start_i:
                ans+=1
                end = min(end,end_i)
            else:
                end =  end_i
        return ans