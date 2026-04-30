class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort by start time so overlapping intervals are adjacent
        intervals.sort(key=lambda x: x[0])
        res = []
        i = 0

        while i < len(intervals):
            if not res or intervals[i][0] > res[-1][1]:
                # No overlap: start a new merged interval
                res.append(intervals[i])
            else:
                # Overlap: merge with the last interval in res
                res[-1][1] = max(res[-1][1], intervals[i][1])
            i += 1

        return res
