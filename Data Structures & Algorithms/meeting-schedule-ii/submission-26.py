import heapq
from typing import List

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List["Interval"]) -> int:
        # Edge case: no meetings => no rooms.
        if not intervals:
            return 0

        # 1) Sort by start time so we process meetings in chronological order.
        intervals.sort(key=lambda it: it.start)

        # Heap stores end times of ongoing meetings (rooms in use).
        min_heap: List[int] = []

        # 2) Process each meeting
        for it in intervals:
            # TODO: if a room is free, reuse it
            # condition must respect "end at t and start at t do NOT conflict"
            if min_heap and min_heap[0] <= it.start:
                # you can take that room so empty it
                heapq.heappop(min_heap)

            # TODO: occupy a room with this meeting's end time
            #
            heapq.heappush(min_heap, it.end)

        # 3) Because heap size never decreases in this one-pop-per-interval formulation,
        # final heap length equals max rooms needed.
        return len(min_heap)
