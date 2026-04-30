class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix= 1, 1
        output = [1] * len(nums)
        # first prefix traverse/scan
        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            output[i] = prefix

        # second suffix traverse/scan
        for i in range(len(nums) - 2 , -1, -1):
            suffix *= nums[i + 1]
            output[i] *= suffix
        return output




# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         # # pre follow up:
#         # output = [1] * len(nums)
#         # for i in range(len(nums)):
#         #     for j in range(len(nums)):
#         #         if i != j:
#         #             output[i] *= nums[j]
#         # return output
#         # post follow up (wtf, we can play smart and for example use power?? or is this bad idea?)
#         # -30 <= nums[i] <= 30 we can make 41 entry hash_table where its key is the num from -30 to 30 and the value is the product without that num.
#         # hash_table = defaultdict(lambda: 1)
#         # for key in range(-30, 31):
#         #     ignore = True
#         #     for num in nums:
#         #         # ignore only once
#         #         if num == key and ignore:
#         #             ignore = False
#         #             continue
#         #         hash_table[key] *= num
#         # return [hash_table[num] for num in nums]
