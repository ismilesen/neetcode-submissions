class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #two pointers. One starts at 0, r starts 1
        #hold onto l value as long as no repeats.
        #increase counter
        #once a repeat is found reset counter.
        #move left to right
        #also store max count
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            res = max(res, r - l + 1)

        
        return res