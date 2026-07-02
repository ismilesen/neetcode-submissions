class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #lets say we have abc, 3
        #we need to hold onto target count
        #then we do a check using a map. Where the map holds frequency and character
        #we make a window for s2 that is size of characters.
        #Once we start checking we, check if the frequency of characters is there and whether or not all characters are there.
        if len(s1) > len(s2):
            return False

        stringMap = Counter(s1)
        stringMap2 = Counter()

        for i in range(len(s1)):
            stringMap2[s2[i]] += 1
            # abc
            # lec 

        if stringMap == stringMap2:
            return True
        
        for r in range(len(s1), len(s2)):
            
            stringMap2[s2[r]] += 1
            l = r - len(s1)
            print(stringMap2)
            if stringMap2[s2[l]] == 1:
                del stringMap2[s2[l]]
            else:
                stringMap2[s2[l]] -= 1
            
            
            if stringMap == stringMap2:
                return True
                
            

        return False