#code tour de jeu

<<<<<<< HEAD
import chess

from affichagePiecesPrises.affichage_prises import AffichagePiecesPrises, TransformationenMatrice


def tourJeu(board, pieces_noires_prises, pieces_blanches_prises):

    numero_tour_joueur = 0
    askAgain = False

    if board.mode == True:
        if not board.isGameFinished():      
            if board.getTurn() == board.WHITE:
                print("C'est au tour des blancs")
                board.move_piece(pieces_noires_prises, pieces_blanches_prises)

            else:
                print("C'est au tour des noirs")
                board.move_piece(pieces_noires_prises, pieces_blanches_prises)

    else : 
        if board.getTurn() == board.WHITE:
            if board.isGameFinished() == False:
                board.move_piece(pieces_noires_prises, pieces_blanches_prises)
            else:
                pass
=======
def tourJeu(board):

    numero_tour_joueur = 0
    joueur_est_blanc = True
    askAgain = False

    if board.mode == True:
        if not board.isGameFinished():
            if board.getTurn() == board.WHITE:
                print("C'est au tour des blancs")
                board.move_piece()

            else:
                print("C'est au tour des noir")
                board.move_piece()

    else : 
        if joueur_est_blanc == True:
            if board.isGameFinished() == False:
                if board.getTurn() == PolyBoard.WHITE:
                    board.move_piece()
                else:
                    pass
>>>>>>> cea0c9ea62cdcb31edaf7ef7603047fd7128e5ed
                    #coup IA a completer


        else :
            if board.isGameFinished() == False:
<<<<<<< HEAD
                if board.getTurn() == board.BLACK:
                    board.move_piece(pieces_noires_prises, pieces_blanches_prises)
                else :
                    pass
                    # coup IA à compléter
    '''
    p = AffichagePiecesPrises(board, coup, TransformationenMatrice(board), board.getTurn())
    print(p)
    if p != None :
        if board.getTurn() == board.WHITE:
            print("les blancs ont prit une piece")
        elif board.getTurn() == board.BLACK:
            print("les noirs ont prit une piece")
    '''
=======
                if board.getTurn() == PolyBoard.BLACK:
                    board.move_piece()
                else :
                    pass
                    # coup IA à compléter
>>>>>>> cea0c9ea62cdcb31edaf7ef7603047fd7128e5ed
