class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        array = nums

        for n in range(len(nums)):
            array.append(nums[n])

        return array