"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Separate and sort start and end times
        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)

        rooms = 0
        max_rooms = 0
        s = e = 0

        # Sweep over time using two pointers
        while s < len(intervals):
            if starts[s] < ends[e]:
                # New meeting starts before the earliest one ends -> need a room
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                s += 1
            else:
                # A meeting has ended (<= case means end at t frees room for start at t)
                rooms -= 1
                e += 1
        print(rooms)
        return max_rooms
