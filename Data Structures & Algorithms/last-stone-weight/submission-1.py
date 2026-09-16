class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        array = sorted(stones)
        while len(array) > 1:
            x = array.pop()
            y = array.pop()
            if x != y:
                array.append(x - y)
                array.sort()
            print(array)
        if not array:
            return 0
        return array[0]