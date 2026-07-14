class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashset = set()

        for num in nums:
            if num not in hashset:
                hashset.add(num)
            else:
                return num
            

        return None