# board.py
EMPTY = 0
P, N, B, R, Q, K = 1, 2, 3, 4, 5, 6

class Move:
    def __init__(self, from_sq, to_sq):
        self.from_sq = from_sq  # (rank,file)
        self.to_sq = to_sq      # (rank,file)
    def __repr__(self):
        return f"{self.from_sq}->{self.to_sq}"

class Board:
    def __init__(self):
        self.board = [[EMPTY]*8 for _ in range(8)]
        self.side_to_move = 1  # 1=white, -1=black

    def setup_start_position(self):
        self.board[6] = [P]*8
        self.board[1] = [-P]*8
        self.board[7][1] = self.board[7][6] = N
        self.board[0][1] = self.board[0][6] = -N

    def apply_move(self, move):
        fr, to = move.from_sq, move.to_sq
        self.board[to[0]][to[1]] = self.board[fr[0]][fr[1]]
        self.board[fr[0]][fr[1]] = EMPTY
        self.side_to_move *= -1

    def undo_move(self, move, captured_piece=EMPTY):
        fr, to = move.from_sq, move.to_sq
        self.board[fr[0]][fr[1]] = self.board[to[0]][to[1]]
        self.board[to[0]][to[1]] = captured_piece
        self.side_to_move *= -1

    def clone(self):
        new_board = Board()
        new_board.board = [row[:] for row in self.board]
        new_board.side_to_move = self.side_to_move
        return new_board
