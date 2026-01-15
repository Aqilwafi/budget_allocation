# movegen.py
from board import P, N, EMPTY, Move

def generate_moves(board):
    moves = []
    side = board.side_to_move
    for r in range(8):
        for f in range(8):
            piece = board.board[r][f]
            if piece == EMPTY or (piece > 0) != (side>0):
                continue
            if abs(piece) == P:
                dr = -1 if side>0 else 1
                tr = r + dr
                if 0<=tr<8:
                    if board.board[tr][f]==EMPTY:
                        moves.append(Move((r,f),(tr,f)))
                    for df in [-1,1]:
                        tc = f+df
                        if 0<=tc<8 and board.board[tr][tc]!=EMPTY and (board.board[tr][tc]>0)!=(side>0):
                            moves.append(Move((r,f),(tr,tc)))
            elif abs(piece) == N:
                offsets = [(-2,-1),(-1,-2),(-2,1),(-1,2),(1,-2),(2,-1),(1,2),(2,1)]
                for dr,df in offsets:
                    tr,tc = r+dr,f+df
                    if 0<=tr<8 and 0<=tc<8:
                        target = board.board[tr][tc]
                        if target==EMPTY or (target>0)!=(side>0):
                            moves.append(Move((r,f),(tr,tc)))
    return moves
