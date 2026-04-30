class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # It is possible to do sorting → then go over each based on indices, when they switch
        # the above method take o(nlog(n)) which is bad.
        hash_table = defaultdict(int)
        for num in nums:
            hash_table[num] += 1
        
        # we can use counting sort on values to return the k top frequent...
        return [key for key,_ in sorted(hash_table.items(), key=lambda item:item[1])][-k:]