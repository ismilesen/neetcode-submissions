class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            count = [0] * 26 # initializes an arry of 26 chars

            for c in s:
                count[ord(c) - ord("a")] += 1

            hashmap[tuple(count)].append(s)
       
        return list(hashmap.values())