class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def comb_sum(target, cur_part, seen):
            nonlocal res
            if target == 0:
                cur_part.sort()
                cur_part_string = str(cur_part)
                if cur_part_string in seen:
                    return
                seen.add(cur_part_string)
                res.append(cur_part.copy())
            for i in range(len(nums)):
                if target - nums[i] < 0:
                    continue
                comb_sum(target - nums[i], cur_part + [nums[i]], seen)
        comb_sum(target, list(), set())
        return res