from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []

        def backtrack(idx: int) -> None:
            # TODO: base case — when idx reaches end, append a COPY of nums to res
            if idx == len(nums):
                res.append(nums.copy())
            # TODO: loop i from idx..end-1
            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                backtrack(idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]

        backtrack(0)
        return res
