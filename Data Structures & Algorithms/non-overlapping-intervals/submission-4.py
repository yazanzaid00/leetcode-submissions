class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1]) # sort by end time
        prev_end, counter = None, 0
        for interval in intervals:
            if not prev_end or interval[0] >= prev_end:
                prev_end = interval[1]
                counter += 1

        return len(intervals) - counter