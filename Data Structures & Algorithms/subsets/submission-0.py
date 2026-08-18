class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lists = [nums, []]
        for n in range(len(nums)):
            for index in range(len(nums)):
                if nums[n] not in lists:
                    lists.append([nums[n]])
                if n + 1 < len(nums) and nums[n + 1]:
                    lists.append([nums[n], nums[n + 1]])

            for combo in combinations(nums, n + 1):
                    lists.append(list(combo))
        unique_data = [list(t) for t in dict.fromkeys(tuple(i) for i in lists)]
        print(lists)
        return unique_data