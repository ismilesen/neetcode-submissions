class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1
        maxP = 0


        #left right pointer
        #if our new profit is higher than our last profit then update
        #else do not

        while r < len(prices):
            
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
                
                

           
        return maxP