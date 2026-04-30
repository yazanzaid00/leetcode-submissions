class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count elements in hash table
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        # Build Frequencies list:
        freq = [None] * (len(nums) + 1)

        for num, frequency in counter.items():
            if freq[frequency]:
                freq[frequency].append(num)
            else:
                freq[frequency] = [num]
        res = []
        for i in range(len(freq) - 1, 0, -1):
            if len(res) == k:
                return res
            if freq[i]:
                res.extend(freq[i])
        return res

        
