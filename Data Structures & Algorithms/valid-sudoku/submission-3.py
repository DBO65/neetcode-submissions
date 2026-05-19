class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        threes = defaultdict(set)

        for r in range(9):
           for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r]:
                    return False
                if board[r][c] in cols[c]:
                    return False
                if board[r][c] in threes[(r//3, c//3)]:
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                threes[(r//3, c//3)].add(board[r][c])

        return True
                
                 