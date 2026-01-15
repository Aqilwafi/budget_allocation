# main.py
from board import Board
from search import choose_best_move_policy
from logger import print_result

b = Board()
b.setup_start_position()

budget = [10000]
depth = 4

best_move = choose_best_move_policy(b, depth, budget)
print_result(b, best_move, budget, depth)
