"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda interval: interval.end)
        solution = []
        for interval in sorted_intervals:
            if not solution or interval.start >= solution[-1].end:
                solution.append(interval)
            

        return len(solution) == len(intervals)