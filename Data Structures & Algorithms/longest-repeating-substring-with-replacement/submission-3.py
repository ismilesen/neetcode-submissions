class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #find highest frequency character
        #In particular window replacements need to be less thjan k.
        #make a window and return counts in hashmap
        #take size of window minus the most repeated character is it less than K?
        #if not then shift l pointer +1 and remove that char frequency minus one.


        l = 0
        charSet = {}
        res = 0

        for r in range(len(s)):
            charSet[s[r]] = 1 + charSet.get(s[r], 0)
            
            if (r - l + 1) - max(charSet.values()) > k:
                charSet[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res