from flask import Flask, jsonify, request
from minesweeper.grid import MineGrid

app = Flask(__name__)
game = None

@app.route("/new_game", methods=["POST"])
def new_game():
    global game
    data = request.get_json()
    rows = data.get("rows", 8)
    cols = data.get("cols", 8)
    mines = data.get("num_mines", 10)
    game = MineGrid(rows, cols, mines)
    return jsonify({"status": "ok", "rows": rows, "cols": cols})

@app.route("/open_cell", methods=["POST"])
def open_cell():
    global game
    if not game:
        return jsonify({"error": "No game"}), 400
    data = request.get_json()
    row = data["row"]
    col = data["col"]
    game.open_cell(row, col)
    grid_view = [[game.grid[r, c] if game.revealed[r, c] else -2
                  for c in range(game.cols)] for r in range(game.rows)]
    return jsonify({"grid": grid_view})

if __name__ == "__main__":
    app.run(debug=True)
