import chess.engine
import platform
import os
import subprocess
import re
import colorama as col

class Eval:
    def __init__(self):
        if platform.system() == 'Windows':
            self.engine = chess.engine.SimpleEngine.popen_uci(os.path.abspath(\
                "../bin//stockfish_14.1_win_x64_popcnt/stockfish_14.1_win_x64_popcnt.exe")) #Prayge
        else: #mac and linux, regex match cuz not same location for at least arch, mac and ubuntu
            res = subprocess.check_output(['which', 'stockfish']).decode("utf-8")
            res = re.findall(r'/usr/[a-z\/]*/stockfish', res)
            self.engine = chess.engine.SimpleEngine.popen_uci(res)


    def betterScore(self, res):
        try :
            if res.relative > chess.engine.Cp(0):
                print("White is winning by " + col.Fore.GREEN + col.Style.BRIGHT + str(res.white().score()/100) + col.Style.RESET_ALL)
            elif res.relative < chess.engine.Cp(0): 
                print("Black is winning by" + col.Fore.RED + col.Style.BRIGHT + str(res.black().score()/100) + col.Style.RESET_ALL)
            else:print("The position is equal")
        except TypeError : #hacky but works #TODO better if time
            if res.relative > chess.engine.Cp(0):
                print("White has" + col.Fore.GREEN + col.Style.BRIGHT + str(res.white().score()) + col.Style.RESET_ALL)
            elif res.relative < chess.engine.Cp(0): 
                print("Black has" + col.Fore.RED + col.Style.BRIGHT + str(res.black().score()) + col.Style.RESET_ALL)
            

    def update(self, board):
        return self.betterScore(self.engine.analyse(\
                    board, chess.engine.Limit(time=1))["score"])
