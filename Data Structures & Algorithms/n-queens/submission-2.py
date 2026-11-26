class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posiDiag = set()
        negDiag = set()
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            
            for c in range(n):
                if c in col or (r + c) in posiDiag or (r - c) in negDiag:
                    continue
                
                col.add(c)
                posiDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                
                backtrack(r + 1)

                col.remove(c)
                posiDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)

        return res