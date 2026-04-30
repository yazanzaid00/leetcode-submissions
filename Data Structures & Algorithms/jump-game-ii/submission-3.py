from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # res = how many jumps we've taken so far (the "level" in BFS)
        res = 0

        # l and r define the current "window" (range of indices) that are reachable
        # with exactly res jumps. Initially we are at index 0 with 0 jumps.
        l = r = 0

        # We stop once our reachable window already includes the last index.
        # While r < len(nums) - 1 means: we haven't yet reached the last index.
        while r < len(nums) - 1:
            # farthest = the farthest index we can reach with one more jump
            # from any index in the current window [l, r].
            farthest = 0

            # This loop corresponds to "looking at the whole green region"
            # in the video: from all indices currently reachable in res jumps,
            # we see how far we can go with one more jump.
            for i in range(l, r + 1):
                # From index i, the farthest we can jump is i + nums[i].
                # We keep the maximum over all i in [l, r].
                farthest = max(farthest, i + nums[i])

            # Now we've fully processed the current layer [l, r].
            # All indices <= r are reachable in res jumps.
            # All new indices in (r, farthest] will be reachable in res + 1 jumps.

            # Move the left boundary to just after the current right boundary.
            # This new [l, r] will represent the next "color" / BFS level.
            l = r + 1

            # The right boundary of the new layer is the farthest we computed.
            r = farthest

            # We've taken one more jump to go from the old layer to the new one.
            res += 1

        # When r >= last index, we've found that res is the minimum number of jumps,
        # because we expanded layers in BFS order (0 jumps, then 1, then 2, ...),
        # and we only move to the next layer after fully exploring the current one.
        return res
