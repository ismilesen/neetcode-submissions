class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #append num if it doesnt match val
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        print(nums)
    
        return k