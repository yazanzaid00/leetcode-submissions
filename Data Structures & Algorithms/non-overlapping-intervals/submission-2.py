class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1]) # sort by end time
        non_overlapping = list()
        for interval in intervals:
            if not non_overlapping or interval[0] >= non_overlapping[-1][1]:
                non_overlapping.append(interval)

        return len(intervals) - len(non_overlapping)