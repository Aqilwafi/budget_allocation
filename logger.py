# logger.py
def print_result(board, best_move, budget, depth, engine_type="Baseline"):
    print(f"=== Engine: {engine_type} ===")
    print("Board position:")
    for row in board.board:
        print(row)
    print(f"Budget remaining: {budget[0]}")
    print(f"Chosen move: {best_move}")
    print(f"Max depth reached: {depth}\n")
