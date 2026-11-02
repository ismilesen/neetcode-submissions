class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        num = 0
        for i in range(len(arr)):
            
            for j in range(i + 1, len(arr)):
                if arr[j] >= num:
                    num = arr[j]
                    print(num)
            
            arr[i] = num
            num = 0
            
        arr[-1] = -1


        return arr

