import chess
import chess.engine

class Eval:
    def __init__(self):
        self.engine = chess.engine.SimpleEngine.popen_uci(r"/tmp/stockfish")

    def betterScore(self, res):
        if res.relative > chess.engine.Cp(0): 
            print(f"White is winning by {res.white().score()/100}")
        elif res.relative < chess.engine.Cp(0): 
            print(f"Black is winning by {res.black().score()/100}")
        else:print("The position is equal")

    def update(self, board):
        return self.betterScore(self.engine.analyse(\
                    board, chess.engine.Limit(time=0.1))["score"])
