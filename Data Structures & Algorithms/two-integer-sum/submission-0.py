class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, number in enumerate(nums):
            difference = target - nums[index]
            if difference in hashmap:
                return [hashmap[difference], index]
     
            hashmap[number] = index
        