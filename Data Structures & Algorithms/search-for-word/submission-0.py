class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        #Board rows and cols hold letters
        #traverse board iterating through columns and rows.
        #words traverse left, right, up, down
        #we need to use backtracking
        ROWS, COLS = len(board), len(board[0])
        #set that holds paths we have traversed
        #if path in set then dont traverse

        path = set()

        #start with r, c 0 and ith letter of our word which is 0 as well and will iterate
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path):
                return False
            
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r - 1, c, i + 1) or 
            dfs(r, c - 1, i + 1))
            path.remove((r,c))
            return res


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True


        return False