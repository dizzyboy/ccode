"""Flask web app for Tic Tac Toe against an AI opponent."""

from flask import Flask, render_template, request, jsonify
from tictactoe import EMPTY, HUMAN, AI, check_winner, is_full, ai_move

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    board = data["board"]  # 3x3 list
    pos = data["position"]  # 0-8
    r, c = divmod(pos, 3)

    # Validate move
    if board[r][c] != EMPTY:
        return jsonify({"error": "Cell is occupied"}), 400

    # Apply human move
    board[r][c] = HUMAN

    # Check if human won or board is full
    winner = check_winner(board)
    if winner:
        return jsonify({"board": board, "winner": HUMAN, "status": "win"})
    if is_full(board):
        return jsonify({"board": board, "winner": None, "status": "draw"})

    # AI responds
    ai_r, ai_c = ai_move(board)
    board[ai_r][ai_c] = AI
    ai_pos = ai_r * 3 + ai_c

    winner = check_winner(board)
    if winner:
        return jsonify({"board": board, "winner": AI, "ai_move": ai_pos, "status": "lose"})
    if is_full(board):
        return jsonify({"board": board, "winner": None, "ai_move": ai_pos, "status": "draw"})

    return jsonify({"board": board, "winner": None, "ai_move": ai_pos, "status": "ongoing"})


if __name__ == "__main__":
    app.run(debug=True)
