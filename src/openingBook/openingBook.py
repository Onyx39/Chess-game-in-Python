import chess
import chess.polyglot

class OpeningBook:
    def __init__(self):
        self.book = chess.polyglot.MemoryMappedReader("./openingBook/Perfect_2021/BIN/Perfect2021.bin")
        self.stop = False

    def entry(self, board):
        if not self.stop:
            try:
                print("The best move is :", self.book.find(board).move)
            except ValueError:
                print("This move is so dumb i don't even have an entry \
                        in my perfet(tm) book opening")
