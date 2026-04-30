class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash table
        B = {}
        for i in range(len(nums)):
            curr = B.get(nums[i])
            if(not curr):
                B[nums[i]] = [i]
            else:
                B[nums[i]].append(i)
        for i in range(len(nums)):
            currList = B.get(target - nums[i], [])
            for index in currList:
                if index != i:
                    return [min(i,index),max(i,index)]

        # Assumptions not reach this
        raise ValueError("Invalid Input")