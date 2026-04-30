class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1]) # sort by end time
        non_overlapping = list()
        last_end = None
        for interval in intervals:
            if not non_overlapping or not last_end or interval[0] >= last_end:
                non_overlapping.append(interval)
                last_end = interval[1]




        return len(intervals) - len(non_overlapping)