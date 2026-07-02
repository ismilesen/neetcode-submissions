class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #h is always greater than number of piles
        #you want to eat as slow as possible to spend all hours eating but need to finish all piles as well
        #Input: piles = [1,4,3,2], h = 9
        #Output: 2
        #took 7hrs to eat at rate of 2. With rate of 1 you would have a pile left over and fail
        #brute force attempt of iterating through k's. We want to do something quicker with binary search
        #max k is largest pile number
        #so in above case its 1-4. Find the smallest k that eats all piles within h hours

        #intital ideas is to sort piles, grab largest.
        #binary search l + r // 2
        
        l, r = 1, max(piles)
        res = r
      

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
               hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
                

        return res