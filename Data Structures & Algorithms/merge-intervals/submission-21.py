class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x : (x[0], x[1])) # sort by time, break ties by end
        for start, end in intervals:
            if not res or res[-1][1] < start:
                res.append([start, end])
            else:
                # mutable list
                res[-1][1] = max(res[-1][1], end)

        return res