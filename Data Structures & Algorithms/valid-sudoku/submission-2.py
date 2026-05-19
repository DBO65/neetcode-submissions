from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for cell in range(9):
                if board[row][cell] == ".":
                    continue
                if board[row][cell] in cols[cell] or board[row][cell] in rows[row] or board[row][cell] in squares[row // 3, cell // 3]:
                    return False

                cols[cell].add(board[row][cell])
                rows[row].add(board[row][cell])
                squares[row // 3, cell // 3].add(board[row][cell])

        return True