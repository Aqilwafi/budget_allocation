# eval.py
from board import P, N, B, R, Q, K, EMPTY

PIECE_VALUES = {P:1, N:3, B:3, R:5, Q:9, K:1000}

def evaluate(board):
    score = 0
    for row in board.board:
        for piece in row:
            if piece != EMPTY:
                score += PIECE_VALUES.get(abs(piece),0) * (1 if piece>0 else -1)
    return score
