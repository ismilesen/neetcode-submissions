class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
            
        l = 0
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in countT and window[c] == countT[c]:
                have += 1
                
            while have == need:
                # Update result if a smaller window is found
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1) # Fixed typo here
                    
                # Shrink the window from the left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
                
        # Removed the destructive pointer overwrite 'l, r = res'
        return s[res[0]:res[1] + 1] if resLen != float("infinity") else ""
