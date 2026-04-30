class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals or len(intervals) <= 0:
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort(key=lambda x:(x[0],x[1])) # sort by start
        res = [intervals[0]]
        i = 1
        while i < len(intervals):
            # if overlapping you need to check the last intervals[i] that is correct 
            if intervals[i][0] <= res[-1][1]:
                res[-1][0] = min(intervals[i][0], res[-1][0])
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
            i += 1

        return res
