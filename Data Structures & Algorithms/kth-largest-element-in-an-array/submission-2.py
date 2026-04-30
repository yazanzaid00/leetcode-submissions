from random import randint
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick select
        def quick_select(start, end, k):
            if start == end:
                return nums[start]
            def partition(start, end):
                i, j = start, end - 1
                while i <= j:
                    if nums[i] > nums[end]:
                        nums[i], nums[j] = nums[j], nums[i]
                        j -= 1
                    else:
                        i += 1
                nums[j + 1], nums[end] = nums[end], nums[j + 1]
                return j + 1
            pivot = randint(start, end)
            nums[pivot], nums[end] = nums[end], nums[pivot]
            curr_idx = partition(start, end)
            if curr_idx == k:
                return nums[curr_idx]
            elif curr_idx > k:
                # search left
                return quick_select(start, curr_idx - 1, k)
            else:
                # search right
                return quick_select(curr_idx + 1, end, k)
        return quick_select(0, len(nums) - 1, len(nums) - k)