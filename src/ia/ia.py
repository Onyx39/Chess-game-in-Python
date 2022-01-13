import chess.engine

class Ia:
    def __init__(self):
        if platform.system() == 'Windows':
            self.engine = chess.engine.SimpleEngine.popen_uci(os.path.abspath(\
                "./src/evalBar//stockfish_14.1_win_x64_popcnt/stockfish_14.1_win_x64_popcnt.exe")) #Prayge
        else: #mac and linux, regex match cuz not same location for at least arch, mac and ubuntu
            res = subprocess.check_output(['whereis', 'stockfish']).decode("utf-8")
            res = re.findall(r'/usr/[a-z\/]*/stockfish', res)
            self.engine = chess.engine.SimpleEngine.popen_uci(res)

    def playMove(self, board):
        self.engine.play(board, chess.engine.Limit(time=1))
        #board.movePiece


