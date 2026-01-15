# search.py (modifikasi)
from movegen import generate_moves
from eval import evaluate
from policy import allocate_budget

def negamax_policy(board, depth, budget, alpha=-float('inf'), beta=float('inf')):
    if depth==0 or budget[0]<=0:
        return evaluate(board)

    max_score = -float('inf')
    moves_budget = allocate_budget(board, budget[0])

    for move, move_budget in moves_budget:
        if budget[0]<=0:
            break
        captured = board.board[move.to_sq[0]][move.to_sq[1]]
        board.apply_move(move)
        old_budget = budget[0]
        budget[0] = move_budget  # gunakan budget alokasi move
        score = -negamax_policy(board, depth-1, budget, -beta, -alpha)
        budget[0] = old_budget - move_budget  # update sisa budget global
        board.undo_move(move, captured)
        if score>max_score:
            max_score = score
        if max_score>alpha:
            alpha=max_score
        if alpha>=beta:
            break
    return max_score

def choose_best_move_policy(board, depth, budget):
    best_score = -float('inf')
    best_move = None
    moves_budget = allocate_budget(board, budget[0])
    for move, move_budget in moves_budget:
        if budget[0]<=0:
            break
        captured = board.board[move.to_sq[0]][move.to_sq[1]]
        board.apply_move(move)
        old_budget = budget[0]
        budget[0] = move_budget
        score = -negamax_policy(board, depth-1, budget)
        budget[0] = old_budget - move_budget
        board.undo_move(move, captured)
        if score>best_score:
            best_score = score
            best_move = move
    return best_move
