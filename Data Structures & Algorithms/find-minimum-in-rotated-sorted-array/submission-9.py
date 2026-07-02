class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search. I think we will do while l < r: l+ r // 2
        #Find a pivot. Have l be first and r be last and mid be l + r // 2
        # if left and mid bigger than r then our target is after mid. make r mid, make mid = l + r // 2
        # if left is bigger than mid and R then our target is before mid. make l mid, and make mid = l + r // 2
        #if left, r and mid equal then rteturn that number

        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            # If mid element is greater than the right element, 
            # the minimum element must be in the right half.
            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, the minimum element is in the left half (including mid).
            else:
                r = mid
                
        # When l == r, they point to the smallest element.
        return nums[l]