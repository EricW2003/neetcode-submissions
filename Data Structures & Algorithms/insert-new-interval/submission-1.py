class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Divide the intervals in 3 groups, the ones before newInterval completely, the ones overlapping and the ones after completely

        before = []
        after = []
        overlapping = []
        
        start, end = newInterval[0],newInterval[1]

        min_start, max_end = start, end
        for element in intervals:
            start_i, end_i = element[0], element[1]

            if end_i<start:
                before.append(element)
            elif start_i>end:
                after.append(element)
            else:
                overlapping.append(element)



        for element in overlapping:
            start_i, end_i = element[0], element[1]
            min_start = min(min_start, start_i)
            max_end = max(max_end, end_i)

        before.append([min_start,max_end])

        return before+after