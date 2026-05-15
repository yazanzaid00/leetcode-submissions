"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = list()
        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, -1))
        
        times.sort()

        max_rooms = 0
        concurent_ctr = 0
        for time in times:
            concurent_ctr += time[1]
            max_rooms = max(max_rooms, concurent_ctr)

        return max_rooms

