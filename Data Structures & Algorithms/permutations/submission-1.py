class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        def permute_dfs(inner_res, res):
            if len(inner_res) == len(nums):
                res.append(inner_res.copy())
                return
            for num in nums:
                if num in visited:
                    continue
                visited.add(num)
                inner_res.append(num)
                permute_dfs(inner_res, res) # need with nums excluding current num and previous chosen nums
                inner_res.pop()
                visited.remove(num) #or discard
        permute_dfs([], res)
        return res