class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        [0, left) we want to have Red == 0
        [left, mid) we want to have white == 1
        [mid, right] we want to explore (unexplored yet)
        (right, len(nums) - 1] there are blue == 2
        """

        left, mid, right = 0, 0, len(nums) - 1
        while left <= mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                # swap between right and mid,
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1

