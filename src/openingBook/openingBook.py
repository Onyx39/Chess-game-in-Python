import chess
import chess.polyglot
import colorama as col

class OpeningBook:
    def __init__(self):
        self.book = chess.polyglot.MemoryMappedReader("../bin/Perfect_2021/BIN/Perfect2021.bin")
        self.stop = False

    def entry(self, board):
        if not self.stop:
            try:
                print("The opening book says : " + col.Fore.MAGENTA + col.Style.BRIGHT + str(self.book.find(board).move) + col.Style.RESET_ALL)
            except (IndexError, ValueError):
                print("The opening book has no entry for this move !")
                self.stop = True
