class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable = {}
        hashtable2 = {}

        for char in s:
            if char in hashtable:
                hashtable[char] += 1
            else:
                hashtable[char] = 1
        
        for char in t:
            if char in hashtable2:
                hashtable2[char] += 1
            else:
                hashtable2[char] = 1
        
        if hashtable == hashtable2:
            return True
        
        return False
        




