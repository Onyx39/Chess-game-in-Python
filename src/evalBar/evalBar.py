import chess
import chess.engine
import platform
import os

class Eval:
    def __init__(self):
        if platform.system()=='Linux':
            self.engine = chess.engine.SimpleEngine.popen_uci(os.path.abspath("/usr/games/stockfish"))
        else:
            self.engine = chess.engine.SimpleEngine.popen_uci(os.path.abspath(\
                "./src/evalBar/stockfish_14.1_win_x64_avx2/stockfish_14.1_win_x64_avx2.exe"))

    def betterScore(self, res):
        try :
            if res.relative > chess.engine.Cp(0):
                print(f"White is winning by {res.white().score()/100}")
            elif res.relative < chess.engine.Cp(0): 
                print(f"Black is winning by {res.black().score()/100}")
            else:print("The position is equal")
        except TypeError : 
            if res.relative > chess.engine.Cp(0):
                print(f"White is winning by {res.white().score()}")
            elif res.relative < chess.engine.Cp(0): 
                print(f"Black is winning by {res.black().score()}")
            

    def update(self, board):
        return self.betterScore(self.engine.analyse(\
                    board, chess.engine.Limit(time=1))["score"])
