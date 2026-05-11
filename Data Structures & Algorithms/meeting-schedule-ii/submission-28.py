"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        ind_intervals = []
        for interval in intervals:
            ind_intervals.append((interval.start, 1))
            ind_intervals.append((interval.end, -1))
        
        ind_intervals.sort()

        max_meetings = 0
        cur_meetings = 0
        for _, delta_state in ind_intervals:
            cur_meetings += delta_state
            max_meetings = max(max_meetings, cur_meetings)
            
        return max_meetings
        
