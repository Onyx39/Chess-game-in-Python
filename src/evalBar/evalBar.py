import chess.engine
import platform
import os
import subprocess
import re

class Eval:
    def __init__(self):
        if platform.system() == 'Windows':
            self.engine = chess.engine.SimpleEngine.popen_uci(os.path.abspath(\
                "./src/evalBar//stockfish_14.1_win_x64_popcnt/stockfish_14.1_win_x64_popcnt.exe")) #Prayge
        else: #mac and linux, regex match cuz not same location for at least arch, mac and ubuntu
            res = subprocess.check_output(['whereis', 'stockfish']).decode("utf-8")
            res = re.findall(r'/usr/[a-z\/]*/stockfish', res)
            self.engine = chess.engine.SimpleEngine.popen_uci(res)


    def betterScore(self, res):
        try :
            if res.relative > chess.engine.Cp(0):
                print(f"White is winning by {res.white().score()/100}")
            elif res.relative < chess.engine.Cp(0): 
                print(f"Black is winning by {res.black().score()/100}")
            else:print("The position is equal")
        except TypeError : #hacky but works #TODO better if time
            if res.relative > chess.engine.Cp(0):
                print(f"White is winning by {res.white().score()}")
            elif res.relative < chess.engine.Cp(0): 
                print(f"Black is winning by {res.black().score()}")
            

    def update(self, board):
        return self.betterScore(self.engine.analyse(\
                    board, chess.engine.Limit(time=1))["score"])
