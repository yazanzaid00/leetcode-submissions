"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sweep line problem
        # we want to handle end time first before start time, we want ends to show before starts because python stable sort
        sweep_line = [(interval.end, -1) for interval in intervals]
        for interval in intervals:
            sweep_line.append((interval.start, +1))
        sweep_line.sort(key=lambda x: x[0])
        curr_rooms = max_rooms = 0
        for dot in sweep_line:
            curr_rooms += dot[1]
            max_rooms = max(max_rooms, curr_rooms)
        return max_rooms