class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #make a hash set, start with biggest number, If biggest number has a num - 1, increment consequtive, if not then end the lookup and send 
        #send consequetive count back, but need to also check other numbs

        hash_set = set(nums)
        longest = 0
        if not hash_set:
            return 0
        for num in hash_set:
            if (num - 1) not in hash_set:
               length = 0
               while (num + length) in hash_set:
                   length += 1
               longest = max(length, longest)
        return longest

