#!/usr/bin/env python3
"""A simple terminal tic-tac-toe game with an AI opponent using minimax."""

import os
import math
import time

EMPTY = " "
HUMAN = "X"
AI = "O"

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def print_board(board):
    print()
    for i in range(3):
        row = " | ".join(board[i])
        print(f"  {row}")
        if i < 2:
            print(" ---+---+---")
    print()

def print_guide():
    print("  Position guide:")
    for i in range(3):
        row = " | ".join(str(i * 3 + j + 1) for j in range(3))
        print(f"  {row}")
        if i < 2:
            print(" ---+---+---")
    print()

def check_winner(board):
    lines = []
    for i in range(3):
        lines.append(board[i])                          # rows
        lines.append([board[r][i] for r in range(3)])   # cols
    lines.append([board[i][i] for i in range(3)])       # diag
    lines.append([board[i][2 - i] for i in range(3)])   # anti-diag

    for line in lines:
        if line[0] != EMPTY and line[0] == line[1] == line[2]:
            return line[0]
    return None

def is_full(board):
    return all(board[r][c] != EMPTY for r in range(3) for c in range(3))

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == EMPTY]

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == AI:
        return 1
    if winner == HUMAN:
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for r, c in get_empty_cells(board):
            board[r][c] = AI
            best = max(best, minimax(board, False))
            board[r][c] = EMPTY
        return best
    else:
        best = math.inf
        for r, c in get_empty_cells(board):
            board[r][c] = HUMAN
            best = min(best, minimax(board, True))
            board[r][c] = EMPTY
        return best

def ai_move(board):
    best_score = -math.inf
    best_move = None
    for r, c in get_empty_cells(board):
        board[r][c] = AI
        score = minimax(board, False)
        board[r][c] = EMPTY
        if score > best_score:
            best_score = score
            best_move = (r, c)
    return best_move

def choose_mode():
    print("  Game modes:")
    print("    1. Player vs AI")
    print("    2. Player vs Player")
    print()
    while True:
        choice = input("  Choose mode (1 or 2): ").strip()
        if choice in ("1", "2"):
            return choice == "1"
        print("  Enter 1 or 2.")

def play():
    clear_screen()
    print("=== Tic Tac Toe ===\n")
    vs_ai = choose_mode()

    board = [[EMPTY] * 3 for _ in range(3)]
    current = "X"

    clear_screen()
    print("=== Tic Tac Toe ===")
    if vs_ai:
        print("  You are X, computer is O")
    print_guide()

    while True:
        print_board(board)

        if vs_ai and current == AI:
            print("  Computer is thinking...")
            time.sleep(0.5)
            r, c = ai_move(board)
            pos_num = r * 3 + c + 1
            print(f"  Computer plays position {pos_num}")
            time.sleep(0.3)
        else:
            label = f"Player {current}" if not vs_ai else "Your"
            try:
                move = input(f"  {label} turn, pick a position (1-9): ").strip()
                if move.lower() == "q":
                    print("  Goodbye!")
                    return
                pos = int(move) - 1
                r, c = divmod(pos, 3)
                if not (0 <= pos <= 8):
                    print("  Enter a number between 1 and 9.")
                    continue
                if board[r][c] != EMPTY:
                    print("  That spot is taken.")
                    continue
            except (ValueError, IndexError):
                print("  Invalid input. Enter 1-9 or 'q' to quit.")
                continue

        board[r][c] = current

        winner = check_winner(board)
        if winner:
            clear_screen()
            print("=== Tic Tac Toe ===")
            print_board(board)
            if vs_ai:
                if winner == HUMAN:
                    print("  You win!")
                else:
                    print("  Computer wins!")
            else:
                print(f"  Player {winner} wins!")
            break

        if is_full(board):
            clear_screen()
            print("=== Tic Tac Toe ===")
            print_board(board)
            print("  It's a draw!")
            break

        current = "O" if current == "X" else "X"
        clear_screen()
        print("=== Tic Tac Toe ===")

    print()
    again = input("  Play again? (y/n): ").strip().lower()
    if again == "y":
        play()

if __name__ == "__main__":
    play()
