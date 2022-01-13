from board.board_and_movment import PolyBoard
import os
import re

if not re.findall(r'src', os.getcwd()):
    os.chdir('./src')

PolyBoard = PolyBoard()
PolyBoard.playGame()
