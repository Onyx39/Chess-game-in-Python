import chess

board = chess.Board()
legal_moves = list(board.legal_moves)
print(legal_moves)

def translate_move():
    res=[]
    for i in range (len(legal_moves)):
        legal_moves[i]=str(legal_moves[i])
        legal_moves[i][15:18]
        res.append(legal_moves[i])
    return res