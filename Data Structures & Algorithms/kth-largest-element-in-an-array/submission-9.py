class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # easy sort return K
        # we can use quick select
        def quick_select(start, end, chosen_ind):
            # start, end is inclusive!
            def partition(start, end):
                # partititon 
                l, r = start, end - 1
                while l <= r:
                    if nums[l] > nums[end]:
                        # swap
                        nums[l], nums[r] = nums[r], nums[l]
                        r -= 1
                    # nums[l] <= nums[end]
                    else:
                        l += 1
                nums[l], nums[end] = nums[end], nums[l]
                return l
                # [3, 1, 2]-> [1, 3, 2]
            if end == start:
                return nums[start]
            if end < start:
                return
            partition_index = partition(start, end)
            if partition_index == chosen_ind:
                return nums[chosen_ind]
            elif partition_index > chosen_ind:
                # go to left
                return quick_select(start, partition_index - 1, chosen_ind)
            else:
                # go to right
                return quick_select(partition_index + 1, end, chosen_ind)
        return quick_select(0, len(nums) - 1, len(nums) - k)