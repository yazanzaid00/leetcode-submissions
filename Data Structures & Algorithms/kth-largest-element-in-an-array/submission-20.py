from random import randint 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # len(nums) - k
        def quick_select(start, end, index_to_search):
            def partition(start, end):
                pivot = end
                l, r = start, end - 1
                # [1,2,3] 
                while l <= r:
                    if nums[l] <= nums[pivot]:
                        l += 1
                    else:
                        nums[l], nums[r] = nums[r], nums[l]
                        r -= 1
                nums[pivot], nums[l] = nums[l], nums[pivot]
                return l
                
            if start == end:
                return nums[start]

            rand_pivot = randint(start, end)
            nums[rand_pivot], nums[end] = nums[end], nums[rand_pivot]
            pivot_index = partition(start, end)
            if pivot_index == index_to_search:
                return nums[pivot_index]
            elif pivot_index < index_to_search:
                # search right 
                return quick_select(pivot_index + 1, end, index_to_search)
            else:
                return quick_select(start, pivot_index - 1, index_to_search)

        return quick_select(0, len(nums) - 1, len(nums) - k)