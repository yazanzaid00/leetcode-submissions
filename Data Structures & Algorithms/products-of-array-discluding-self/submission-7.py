class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # pre follow up:
        # output = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             output[i] *= nums[j]
        # return output
        # post follow up (wtf, we can play smart and for example use power?? or is this bad idea?)
        # -20 <= nums[i] <= 20 we can make 41 entry hash_table where its key is the num from -20 to 20 and the value is the product without that num.
        hash_table = defaultdict(lambda: 1)
        for key in range(-30, 31):
            ignore = True
            for num in nums:
                # ignore only once
                if num == key and ignore:
                    ignore = False
                    continue
                hash_table[key] *= num
        return [hash_table[num] for num in nums]
