from heapq import heapify_max, heappop_max, heappush_max
from typing import Dict


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # For LeetCode: fixed alphabet 'a', 'b', 'c'.
        counts: Dict[str, int] = {
            "a": a,
            "b": b,
            "c": c,
        }
        return self._build_happy_string(counts)

    def _build_happy_string(self, counts: Dict[str, int]) -> str:
        """
        Generic helper: given a dict char -> count, build the longest
        'happy' string (no three identical chars in a row).
        Works for any number of distinct characters.
        """

        # Build a max-heap: (remaining_count, char) for all chars with count > 0.
        heap = [(cnt, ch) for ch, cnt in counts.items() if cnt > 0]
        if not heap:
            return ""

        heapify_max(heap)

        result: list[str] = []

        while heap:
            used_char = False      # Did we manage to append something this round?
            skipped: list[tuple[int, str]] = []  # Temporarily skipped candidates

            # Try candidates from most frequent to less frequent
            while heap and not used_char:
                count, ch = heappop_max(heap)

                # If appending this char would create 'xxx', we can't use it now.
                if len(result) >= 2 and result[-1] == result[-2] == ch:
                    skipped.append((count, ch))
                    continue

                # Safe to use this character once.
                result.append(ch)
                count -= 1

                # If we still have more of this char, push it back with updated count.
                if count > 0:
                    heappush_max(heap, (count, ch))

                used_char = True

            # Return all skipped candidates to the heap (unchanged counts).
            for item in skipped:
                heappush_max(heap, item)

            # If we couldn't use any candidate, we are done:
            # no character can be appended without violating the rules.
            if not used_char:
                break

        return "".join(result)
