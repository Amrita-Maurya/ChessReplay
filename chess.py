import chess_game
import chess
import chess.pgn
import chess.svg
from chessboard import display
from time import sleep 

board = chess_game.Board()

pgn_file = open("C:/Users/hp/Desktop/WISE PYTHON/WorldChamp2010.pgn")

game = chess.pgn.read_game(pgn_file)

board = game.board()
game_board = display.start()
sleep(2)
for move in game.mainline_moves():
    board.push(move)
    display.update(board.fen(), game_board)
    sleep(0.5)
    if not game_board.flipped:
        display.flip(game_board)

pgn_file.close()
result = game.headers["Result"]
if result == "1-0":
    print(game.headers["White"], "in White won the game!")
elif result == "0-1":
    print(game.headers["Black"], "in Black won the game!")
else:
    print("It's a tie!")
