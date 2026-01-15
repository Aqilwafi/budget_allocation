# logger.py
def print_result(board, move, budget, depth):
    print("Position: (simplified board)")
    for row in board.board:
        print(row)
    print(f"Budget: {budget[0]} nodes remaining")
    print(f"Chosen move: {move}")
    print(f"Max depth reached: {depth}")
