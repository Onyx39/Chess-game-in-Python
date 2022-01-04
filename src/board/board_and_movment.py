import chess

board = chess.Board()
#board de base : chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')

board.legal_moves   # Met en oeuvre et vérifie si le mouvement qui est effectué est légal ou non

def traduction(string):
    if string == "1" :
        return str('.')
    if string == "2" :
        return str('. .')
    if string == "3" :
        return str('. . .')
    if string == "4" :
        return str('. . . .')
    if string == "5" :
        return str('. . . . .')
    if string == "6" :
        return str('. . . . . .')
    if string == "7" :
        return str('. . . . . . .')
    if string == "8" :
        return str('. . . . . . . .')
    else : return string


def affichage_plateau(board):
    copie = board.epd()
    compteur = 0
    ch = ""
    #print("    A B C D E F G H ")
    print("   ___________________")
    print("  |                   |")
    for j in copie :
        if j != "/" :
            ch += traduction(j) + " "
        else : 
            print(8 - compteur, '| ', ch, '|', 8 - compteur)
            compteur += 1
            ch = ""
    print("1", '| ', ch[0:16], '|', "1")
    print("  |___________________|")
    print("     A B C D E F G H")
  
print (affichage_plateau(board))

def detect_echec():
    if board.is_checkmate() == False and board.is_check() == False:
        print('La partie continue')
    elif board.is_checkmate() == False and board.is_check() == True:
        print('Echec')
    elif board.is_checkmate() == True:
        print('Echec et Mat')
             

def move_piece(str):
    #str est du type "'case de départ' 'case d'arrivée'" (ex: 'e2e3' bouge la piece de e2 à e3)
    board.push_san(str)
    affichage_plateau(board)
    print(affichage_plateau(board))
    detect_echec()