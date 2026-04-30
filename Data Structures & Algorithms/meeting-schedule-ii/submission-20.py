"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        points = list()
        for interval in intervals:
            points.append((interval.start, 1))
            points.append((interval.end, -1))
        points.sort(key = lambda x:(x[0], x[1])) # break the ties on the end...
        max_count = curr_count = 0

        for point in points:
            curr_count = max(curr_count + point[1], 0)
            max_count = max(max_count, curr_count)
        return max_count
