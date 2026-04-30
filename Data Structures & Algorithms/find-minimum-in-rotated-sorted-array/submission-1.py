class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l and r define the current search window [l, r]
        l, r = 0, len(nums) - 1
        
        # We keep shrinking [l, r] until it collapses to a single index
        while l < r:
            # Standard way to compute mid without overflow
            m = (r + l) // 2

            # Key idea: compare middle with rightmost element
            # nums[r] is always in the "right" sorted chunk
            # If nums[m] > nums[r], mid is in the left chunk
            #   => the minimum must be strictly to the right of m
            if nums[m] > nums[r]:
                # Discard [l..m], search in (m..r]
                l = m + 1
            else:
                # Otherwise nums[m] <= nums[r], so mid is in the right chunk
                # The minimum is in [l..m], so we discard (m..r]
                r = m
                
        # When l == r, the window has collapsed to the index of the minimum
        return nums[l]
