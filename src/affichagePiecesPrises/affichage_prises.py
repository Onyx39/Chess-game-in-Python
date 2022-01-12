import chess


def Reduction_str_Board(board) :
    b = board.epd()
    l = []
    i = 0

    while b[i] != ' ' :
        l.append(b[i])
        i += 1

    return l 

    
def Affichage_cases_vides (n) :
    l = []
    for i in range (n) :
        l.append('.')
    return l


def TransformationenMatrice(pboard) :        #TRANSFORMER LA STR EN MATRICE 
    b = Reduction_str_Board(pboard.board)
    mat_board = []
    n=0
    
    i = 0
    for j in range(8) :
        l=[]
        while  i<len(b) and b[i] != '/' :
            i +=1
        for i in range (n,i,1) : 
            if b[i] == '1' or  b[i] == '2' or  b[i] == '3' or  b[i] == '4' or  b[i] == '5' or  b[i] == '6' or  b[i] == '7' or  b[i] == '8' or  b[i] == '9' :
                l += Affichage_cases_vides(int(b[i]))
            else : l.append(b[i])
        n = i +2
        
        mat_board.append(l)
        i+=2

    return mat_board

def AffichagePiecesPrises(board, mouvement, b_transforme, tour_joueur_blanc) :
    
    l = 0
    col = 0

    joueur_noir_piece_blanche_prise = None
    joueur_blanc_piece_noire_prise = None

    l = 8-int(mouvement[3])

    if mouvement[2] == 'a' :
        col = 0
    elif mouvement[2] == 'b' :
        col = 1
    elif mouvement[2] == 'c' :
        col = 2
    elif mouvement[2] == 'd' :
        col = 3
    elif mouvement[2] == 'e' :
        col = 4
    elif mouvement[2] == 'f' :
        col = 5
    elif mouvement[2] == 'g' :
        col = 6
    elif mouvement[2] == 'h' :
        col = 7
    

    if b_transforme[l][col] == '.' : # board.is_en_passant(chess.Move(mouvement)) == False :
        return joueur_blanc_piece_noire_prise, joueur_noir_piece_blanche_prise
    else : 
        if False and board.is_en_passant(chess.Move(mouvement)) == True :
            if compteur_tour %2 == 1 :
                piece_blanche_prise = b_transforme[l][col]
            else :
                piece_noire_prise = b_transforme[l+1][col] 
        #if board.getTurn() == PolyBoard.BLACK:
        if tour_joueur_blanc == False :
            if b_transforme[l][col] == 'r' :
                return joueur_blanc_piece_noire_prise, joueur_noir_piece_blanche_prise
            else :
                joueur_noir_piece_blanche_prise = b_transforme[l][col]
        else :
            if b_transforme[l][col] == 'R' :
                return joueur_blanc_piece_noire_prise, joueur_noir_piece_blanche_prise
            else :
                joueur_blanc_piece_noire_prise = b_transforme[l][col]

    return joueur_blanc_piece_noire_prise, joueur_noir_piece_blanche_prise


if __name__ == '__main__' :
    
    #TEST TRANSFORMATION MATRICE ET AFFICHAGE DES PIECES PRISE MOUVEMENT SIMPLE
    '''
    board = chess.Board()
    b = TransformationenMatrice(board)
    board = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
    print(board.epd())
    print(Reduction_str_Board(board))
    print(Affichage_cases_vides(6))
    print(TransformationenMatrice(board))
    print(AffichagePiecesPrises(board, 'e3a1', b, 1, False))
    print(AffichagePiecesPrises(board, 'e3a1', b, 1, False))
    print(AffichagePiecesPrises(board, 'e3a1', b, 1, True))
    print(AffichagePiecesPrises(board, 'e3a1', b, 1, True))
    '''
