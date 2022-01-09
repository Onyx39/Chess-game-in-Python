import chess
import chess.polyglot
from src.board.board_and_movment import board 

Book = chess.polyglot.MemortyMapperReader("./Perfect_2021/Perfect2021.bin")

res = Book.find(board)
print(res)
