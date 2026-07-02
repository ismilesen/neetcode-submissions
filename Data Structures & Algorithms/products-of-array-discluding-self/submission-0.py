class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res_list = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res_list[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res_list[i] *= suffix
            suffix *= nums[i]
        return res_list
      