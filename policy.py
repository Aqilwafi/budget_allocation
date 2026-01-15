# policy.py
from eval import evaluate
from movegen import generate_moves

def allocate_budget(board, total_budget):
    """
    Return a list of (move, allocated_budget) tuples.
    Dummy policy: alokasikan lebih banyak budget ke move
    yang secara heuristik punya score lebih tinggi.
    """
    moves = generate_moves(board)
    if not moves:
        return []

    # Hitung evaluasi cepat untuk setiap move
    move_scores = []
    for move in moves:
        board.apply_move(move)
        score = evaluate(board)
        board.undo_move(move)
        move_scores.append((move, score))

    # Normalisasi scores → persentase
    min_score = min(score for move, score in move_scores)
    max_score = max(score for move, score in move_scores)
    score_range = max_score - min_score + 1e-5  # hindari div by zero

    allocated = []
    for move, score in move_scores:
        proportion = (score - min_score) / score_range
        # alokasi minimal 10% budget per move
        move_budget = max(int(total_budget * proportion), max(int(total_budget*0.1), 1))
        allocated.append((move, move_budget))

    # Sesuaikan total budget agar tidak lebih dari total_budget
    total_allocated = sum(b for m,b in allocated)
    scale = total_budget / total_allocated
    allocated = [(m, int(b*scale)) for m,b in allocated]

    return allocated
