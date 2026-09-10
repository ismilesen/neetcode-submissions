class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #need to check if the queen can attack left, right, up and down
        #when checking if the queen can attack we check if any other queens are in the way
        #problem is finding a solution that allows all n queens, depending on n the solution changes
        #it would be easy if we could always start placing the first queen at 0,0
        #but we need to return distinct solutions which is kind of crazy
        #what we can do is start with placing first queen on any of the n tiles of row 1.
        #we go through all and for the next rows we only try to place where it wont come in contact with previous queens
        #we only return successful boards.
        #for a board to be successful it has to pass our conditions and not trigger the fail conds
        boards = []
        board = [["."] * n for i in range(n)]
        def backtrack(row):
            #call itself 
            #call isSafe
            if row == n:
                copy = ["".join(row) for row in board]
                boards.append(copy)
                return
            for col in range(n):
                safe = self.isSafe(row, col, board)
                if safe:
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."
            
        
        backtrack(0)
        return boards
        
        #three conds to check: diag, vert, horiz
        #queen placed on (0, n)
        #check (0 + 1, n ) until finish
        #check (0 - 1, n) until 0
        #check (0, n - 1)
        #check (0, n + 1)
        #check (0 + 1, n + 1)
        #check (0 - 1, n - 1)
        #check (0 + 1, n - 1)
        #check (0 - 1, n + 1)
        #at the end of our backtracking
    def isSafe(self, r: int, c: int, board):
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1

        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        return True