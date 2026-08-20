class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        nums.sort()
        for num in nums:
        # For every existing subset, create a new one containing the current number
            subsets += [current + [num] for current in subsets]
        unique_matrix = [list(item) for item in set(tuple(i) for i in subsets)]
        return unique_matrix