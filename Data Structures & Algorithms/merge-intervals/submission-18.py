class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0]) # sort by start
        res = []
        max_end = None
        i = 0
        while (i < len(intervals)):
            # there is no overlap
            if (max_end is None or intervals[i][0] > max_end):
                res.append(intervals[i])
                max_end = intervals[i][1] if max_end is None else max(max_end, intervals[i][1])
                i += 1
            else:
                # there is an overlap
                min_start = None
                while(i < len(intervals) and intervals[i][0] <= max_end):
                    # get the longest interval
                    min_start = intervals[i - 1][0] if min_start is None else min(min_start, intervals[i][0])
                    max_end = max(max_end, intervals[i][1])
                    i += 1
                res[-1] = [min_start, max_end]
        return res