class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Idea:
        # Build combinations in non-decreasing order (by index), so we generate each combination once.
        # Sorting enables pruning: if nums[i] > remaining, all later nums are also too big.

        nums.sort()
        res: List[List[int]] = []
        cur: List[int] = []

        def dfs(start: int, remaining: int) -> None:
            # Invariant:
            # - cur contains a non-decreasing sequence of chosen numbers (by index >= start history)
            # - sum(cur) + remaining == target
            # - We only choose next elements from nums[start:] to prevent permutations duplicates.

            # TODO (base case 1): if remaining == 0 -> found a valid combination:
            #   - append a COPY of cur to res
            #   - return (do not extend further)
            if remaining == 0:
                res.append(cur.copy())
                return
            # Loop choices: try each candidate from 'start' onward (reuse allowed => recurse with same i)
            for i in range(start, len(nums)):
                x = nums[i]

                # Pruning (works because nums is sorted):
                # If x is too large, all later numbers are too large too -> stop exploring this path.
                # TODO: 
                if x > remaining: break
                # Choose x
                cur.append(x)

                # Recurse:
                # Reuse allowed -> we pass i (not i+1) so x can be chosen again.
                dfs(i, remaining - x)

                # Backtrack (undo choice)
                cur.pop()

        dfs(0, target)
        return res
