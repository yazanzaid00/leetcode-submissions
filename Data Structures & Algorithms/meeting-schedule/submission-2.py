"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda interval:interval.start)
        solution = []
        for interval in intervals:
            if not solution or interval.start >= solution[-1].end:
                solution.append(interval)
            

        return len(solution) == len(intervals)