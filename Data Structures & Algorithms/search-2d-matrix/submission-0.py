class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #check the max count of the row
        #if its higher than target go back a row or else move forward.
        #check if beginning and end actually

        

        for r_idx, row in enumerate(matrix):
            for c_idx, val in enumerate(row):
                if val == target:
                    return True

        return False