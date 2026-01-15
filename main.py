# main.py
from board import Board
from search import choose_best_move_policy
from logger import print_result

# Contoh dataset board
dataset = [
    ([[0, 0, 0, 0, 0, 0, 0, 0],
      [0, -1, -1, -1, -1, -1, -1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 1, 1],
      [0, 0, 0, 0, 0, 0, 0, 0]], 1)
]

budget_value = 10000  # total node budget per run
depth_value = 4

for idx, (board_array, stm) in enumerate(dataset):
    print(f"--- Running board {idx+1} ---")
    
    # ===== Baseline =====
    b_base = Board()
    b_base.setup_board(board_array, stm)
    budget_base = [budget_value]  # copy budget for this run
    best_move_base = choose_best_move_policy(b_base, depth_value, budget_base)
    print_result(b_base, best_move_base, budget_base, depth_value, engine_type="Baseline")
    
    # ===== Policy / Metode =====
    b_policy = Board()
    b_policy.setup_board(board_array, stm)
    budget_policy = [budget_value]  # reset budget for policy run
    best_move_policy = choose_best_move_policy(b_policy, depth_value, budget_policy, use_policy=True)
    print_result(b_policy, best_move_policy, budget_policy, depth_value, engine_type="Policy")
